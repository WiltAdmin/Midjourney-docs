**Remix**

**Use Remix Mode to change prompts, parameters, model versions, or aspect ratios between variations. Remix will take the general composition of your starting image and use it as part of the new Job. Remixing can help change the setting or lighting of an image, evolve a subject, or achieve tricky compositions.**

Remix is an experimental feature that may change or be removed at any time.

**Using Remix**

Activate Remix mode with the /prefer remix command or by using the /settings command and toggling the 🎛️ Remix Mode button. Remix changes the behavior of the variation buttons (V1, V2, V3, V4) under image grids. When Remix is enabled, it allows you to edit your prompt during each variation. To Remix an upscale select 🪄 Make Variations.

When Remix is enabled, Variation buttons turn green when used instead of blue.You can switch [Model Versions](https://docs.midjourney.com/models) when using Remix.When you are done with Remix use the /settings or /prefer remix command to turn it off.Create a standard image variation when Remix is active by not modifying the prompt in the pop-up window.

**Step 1**

line-art stack of pumpkins

MJ\_Remix\_1.png ¬

**Turn on Remix mode.**

Select an image grid or upscaled image to Remix.

**Step 2**

Remix

MJ\_Remix2.png ¬

**Select "Make Variations."**

Modify or enter a new prompt in the pop-up.

**Results**

pile of cartoon owls

MJ\_Remix3.png ¬

The Midjourney Bot generates an image using the new prompt with influence from the original image.

**Starting Image**

MJ\_Remix\_StackPumpkins.jpg ¬

line-art stack of pumpkins

**Model Change**

MJ\_Remix\_testp.jpg ¬

line-art stack of pumpkins --test

**Subject Change**

MJ\_Remix\_Balloons.jpg ¬

balloon-animal shaped stack of pumpkins"

**Medium Change**

MJ\_Remix\_Fruit.jpg ¬

vibrant illustrated stack of fruit

**Using Parameters with Remix**

You can add or remove [Parameters](https://docs.midjourney.com/parameter-list) while using Remix mode, but you must use valid parameter combinations. Changing /imagine prompt illustrated stack of pumpkins --version 3 --stylize 10000 to illustrated stack of pumpkins --version 4 --stylize 10000 will return an error because Midjourney Model Version 4 is incompatible with the Stylize parameter.

Only parameters that normally influence variations will work while using Remix:

||<p>**Affects Initial** </p><p>**Generation**</p>|<p>**Affects Variations** </p><p>**and Remix**</p>|
| :-: | :-: | :-: |
|Aspect Ratio\*|✓|✓|
|Chaos|✓||
|Image Weight|✓||
|No|✓|✓|
|Quality|✓||
|Seed|✓||
|Same Seed|✓||
|Stop|✓|✓|
|Stylize|✓||
|Tile|✓|✓|
|Video|✓|✓|
- Changing aspect ratios with Remix will *stretch* an image. It will not extend the canvas, add missing details, or fix a bad crop.

**How to Activate Remix**

**Use the Settings Command**

Type /settings and select Remix from the pop-up.🎛️ Remix

**Use the Prefer Remix Command**

Type /prefer remix to toggle Remix mode on and off.MJ\_preferRemix.png ¬
