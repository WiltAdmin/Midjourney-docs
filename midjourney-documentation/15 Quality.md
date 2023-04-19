**Quality**

**The --quality or --q parameter changes how much time is spent generating an image. Higher-quality settings take longer to process and produce more details. Higher values also mean more GPU minutes are used per job. The quality setting does not impact resolution.**

The default --quality value is 1. Higher values use more of your subscription's GPU minutes.--quality accepts the values: .25, .5, and 1 for the default model. Larger values will be rounded down to 1.--quality only influences the initial image generation.--quality works with [Model Versions](https://docs.midjourney.com/models) 1, 2, 3, 4, 5 and niji.

**Quality Settings**

Higher --quality settings aren't always better. Sometimes a lower --quality settings can produce better results—depending on the image you're trying to create. Lower --quality settings might be best for a gestural abstract look. Higher --quality values may improve the look of architectural images that benefit from many details. Choose the setting that best matches the kind of image you're hoping to create.

Prompt example: /imagine prompt woodcut birch forest --q .25

**Version 4**

**--quality .25**

MJ\_Quality\_025.jpg ¬

\-

quickest results, least detailed results

*4× faster and ¼ the GPU minutes.*

**--quality .5**

MJ\_Quality\_05.jpg ¬

🔥 Half Quality

Less detailed results

*2× faster and ½ the GPU minutes.*

**--quality 1**

MJ\_Quality\_1.jpg ¬

🔥 Base Quality

The default setting

*Well balanced between detail and speed*

**Version 5**

**--quality .25**

MJ\_V5\_Quality\_025.jpg ¬

\-

quickest results, least detailed results

*4× faster and ¼ the GPU minutes.*

**--quality .5**

MJ\_V5\_Quality\_05.jpg ¬

🔥 Half Quality

less detailed results

*2× faster and ½ the GPU minutes.*

**--quality 1**

MJ\_V5\_Quality\_1.jpg ¬

🔥 Base Quality

the default setting

*Well balanced between detail and speed*


**Version Quality Compatibility**

|**Model Version**|**Quality .25**|**Quality .5**|**Quality 1**|**Quality 2**|
| :-: | :-: | :-: | :-: | :-: |
|Version 5|✓|✓|✓|-|
|**Version 4**|✓|✓|✓|-|
|Version 3|✓|✓|✓|✓|
|Version 2|✓|✓|✓|✓|
|Version 1|✓|✓|✓|✓|
|niji|✓|✓|✓|-|


**How to Use the Quality Parameter**

**Use the --quality or --q Parameter**

Add --quality <value> or --q <value> to the end of your prompt.

MJ\_Parameter\_Quality.gif ¬

**Use the Settings Command**

Type /settings and select your preferred quality value from the menu.

🔥 Half Quality 🔥 Base Quality 🔥 High Quality (2x cost)
