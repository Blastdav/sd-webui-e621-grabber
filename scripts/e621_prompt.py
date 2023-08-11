import gradio as gr

from modules import scripts, script_callbacks
from modules.shared import opts, OptionInfo
from modules.ui_components import FormRow, FormColumn, FormGroup, ToolButton

import re
import requests

NAME = "e621 Grabber"


class Script(scripts.Script):

  def title(self):
    return NAME


  def show(self, _is_img2img):
    return scripts.AlwaysVisible


  def grab(self,tags):
    tags += " " + opts.tag_additions
    tags = tags.replace("<", "%3C").replace(">", "%3E").replace(":", "%3A").replace(" ", "+").replace("<", "%3C")
    taglist = []
    headers = {"User-Agent": "e6grabber/0.1 (by /u/yourusernamehere)"}

    url = "https://e621.net/posts.json?tags=" + tags + "&limit=1"
    r = requests.get(url, headers=headers)
    json = r.json()
    for post in json["posts"]:
        taglist.append(post["tags"]["general"])
    
    regexRemove = opts.regex_remove
    regexIncrease = opts.regex_weight.split(",")
    regexDoubleIncrease = opts.regex_extra_weight.split(",")

    clean_list = []

    for image_post in taglist:

        clean_image_post = []

        for tag in image_post:
            if "<" in tag:
                continue
            if re.match(regexRemove, tag):
                continue
            if tag in regexIncrease:
                tag = "(" + tag + ":" + opts.weight + ")"
            if tag.replace("(","").replace(":" + opts.weight + ")","") in regexDoubleIncrease:
                tag = "(" + tag + ")"
            if "_" in tag:
                tag = tag.replace("_", " ")
            
            clean_image_post.append(tag)

        clean_list.append(clean_image_post)

    return_list = []
    # if count == 1:
    return_list.append(",".join(clean_list[0]))
    # else:
    #     for x in clean_list[0:count]:
    #       return_list.append(",".join(x))
    if len(return_list) == 0:
      print("No results found")
      return ""
    return ",".join(return_list)


  def process(self, p, source, is_this_thing_enabled, randomize, *script_args, **kwargs):

    if not is_this_thing_enabled:
      return
    
    if not randomize:
      print("Not randomizing")
      prompt_add = self.grab(source)
      for i, prompt in enumerate(p.all_prompts):
        positivePrompt = prompt_add + ", " + prompt
        p.all_prompts[i] = positivePrompt
    else:
      print("One moment, grabbing prompts...")
      for i, prompt in enumerate(p.all_prompts):
        positivePrompt = self.grab(source) + ", " +  prompt
        p.all_prompts[i] = positivePrompt
    pass


  def before_component(self, component, **kwargs):
    # Find the text2img textbox component
    if kwargs.get("elem_id") == "txt2img_prompt": #postive prompt textbox
      self.boxx = component
    # Find the img2img textbox component
    if kwargs.get("elem_id") == "img2img_prompt":  #postive prompt textbox
      self.boxxIMG = component


  def ui(self, _is_img2img):
    with gr.Group():
      with gr.Accordion(NAME, open=True):
        with FormRow():
           
          with FormColumn(min_width=160):
            is_this_thing_enabled = gr.Checkbox(value=False, label="Enable", info="Enable Or Disable E621 Grabber")
          with FormColumn(elem_id="Randomize"):
            randomize = gr.Checkbox(value=False, label="Enabled", info="Random prompt every time")

        source = gr.Textbox(label="Source", value="", placeholder="Search query")

        # with FormRow():
        #   with FormColumn(min_width=160):
        #     generate_btn = gr.Button("Add to prompt", variant="primary")
        #     generate_btn.click(fn=self.grabadd, inputs=[source, self.boxx], outputs=[self.boxx])

    return [source,is_this_thing_enabled,randomize] #generate_btn
  
  # def grabadd(self, source, prompt_box):
  #   add_text = self.grab(source)
  #   if prompt_box == "":
  #     return add_text
  #   else:
  #     return prompt_box + ", " + add_text
    

def on_ui_settings():

  section = ("e621-grabber", NAME)

  settings_options = [
    # ("e621_grabber_username", "", "e621 Username. Not required, but highly preferred"),
    # ("e621_grabber_api_key", "", "e621 API Key. Not required, but highly preferred"),
    ("tag_additions","-text -human -skull -animated -scat -watersports -fat -comic -meme order:random score:>1000","Things to include with every search (Best to include order:random and possibly score:>1000)"),
    ("regex_remove","(black_and_white|black|blue|brown|gold|gradient|green|grey|monotone|multicolored|amber|orange|pink|purple|red|spotted|striped|tan|two_tone|white|yellow|blonde)_(fur|body|hair|eyes|nose|scales|ears|glans|penis|perineum|balls|pawpads|anus|nipples|tongue|sclera|markings|spots|tail|pussy|nipples|penis|genita|skin|areola|inner_pussy|claws|lips|hair|eyebrows|pupils|feathers|foreskin|wings|mouth|clitoris|flesh|clitoral_hood|sheath|beak)","Regex of tags to remove (regex)"),
    ("regex_weight","","Tags to increase the weight of (comma separated)"),
    ("regex_extra_weight","","Tags to add extra brackets around (comma separated)"),
    ("weight","1.3","Amount of weight to add to tags")
  ]

  for setting_name, *data in settings_options:
    opts.add_option(setting_name, OptionInfo(*data, section=section))

script_callbacks.on_ui_settings(on_ui_settings)
