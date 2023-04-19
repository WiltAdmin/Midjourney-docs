**Image Prompts**

**You can use images as part of a prompt to influence a Job's composition, style, and colors. Images prompts can be used alone or with text prompts—experiment with combining images with different styles for the most exciting results.**

To add images to a prompt, type or paste the web address where the image is stored online. The address must end in an extension like .png, .gif, or .jpg. After adding image addresses, add any additional text and parameters to complete the prompt.

MJ Prompt.png ¬


Image prompts go at the front of a prompt.Prompts must have two images or one image and additional text to work.An image URL must be a direct link to an online image.In most browsers, right-click or long-press an image and select Copy Image Address to get the URL.The [/blend command](https://docs.midjourney.com/blend) is a simplified image prompting process optimized for mobile users.

**Upload an image to Discord**

To use a personal image as part of a prompt, upload it to Discord. To upload an image, click the **Plus** sign next to where messages are typed. Select **Upload a File**, select an image, and send the message. To add this image to a prompt, begin typing /imagine as usual. After the prompt box appears, drag the image file into the prompt box to add the image's URL. Alternatively, right-click the image, select **Copy Link**, and then paste the link within the prompt box.

Discord\_FHZfwDLhLY.gif ¬

Privacy Notes

Upload images in your Direct Messages with the Midjourney Bot to prevent other server users from seeing an image.Image prompts are visible on the Midjourney website unless a user has Stealth Mode.


**Examples**

**Starting Images**

MJ\_ImagePrompt\_Statue.png ¬

Statue of Apollo

MJ\_ImagePrompt\_Flowers.png ¬

Vintage Flower Illustration

MJ\_ImagePrompt\_Jelly.jpg ¬

Ernst Haeckel's Jellyfish

MJ\_ImagePrompt\_Lichen.png ¬

Ernst Haeckel's Lichen

MJ\_ImagePrompt\_Wave.png ¬

Hokusai's The Great Wave

**Midjourney Model Version 4**

**Statue + Flowers**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Flowers.png ¬

MJ\_ImagePrompt\_Statue\_Flowers.png ¬

**Statue + Jellyfish**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Jelly.jpg ¬ MJ\_ImagePrompt\_Statue\_Jelly.png ¬

**Statue + Lichen**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Lichen.png ¬ MJ\_ImagePrompt\_Statue\_Litchen.png ¬

**Statue + Wave**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Wave.png ¬ MJ\_ImagePrompt\_Statue\_Wave.png ¬

**Statue + Lichen + Flowers**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Lichen.png ¬ + MJ\_ImagePrompt\_Flowers.png ¬ MJ\_ImagePrompt\_Statue\_lichen\_flowers.png ¬



**Midjourney Model Version 5**

**Statue + Flowers**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Flowers.png ¬

MJ\_V5\_ImagePrompt\_Statue\_Flowers.jpg ¬

**Statue + Jellyfish**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Jelly.jpg ¬ MJ\_V5\_ImagePrompt\_Statue\_Jellyfish.jpg ¬

**Statue + Lichen**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Lichen.png ¬ MJ\_V5\_ImagePrompt\_Statue\_Lichen.jpg ¬

**Statue + Wave**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Wave.png ¬ MJ\_V5\_ImagePrompt\_Statue\_Wave.jpg ¬

**Statue + Lichen + Flowers**

MJ\_ImagePrompt\_Statue.png ¬ + MJ\_ImagePrompt\_Lichen.png ¬ + MJ\_ImagePrompt\_Flowers.png ¬ MJ\_V5\_ImagePrompt\_Statue\_Flowers\_Lichen.jpg ¬

Aspect Ratio Tip

Crop images to the same aspect ratio as your final image for the best results.


**Image Weight Parameter**

Use the image weight parameter --iw to adjust the importance of the image vs. text portion of a prompt. The default value is used when no --iw is specified. Higher --iw values mean the image prompt will have more impact on the finished job.

See the [Multi Prompts](https://docs.midjourney.com/multi-prompts) page for more information about the relative importance between parts of a prompt.

Different [Midjourney Version Models](https://docs.midjourney.com/models) have different image weight ranges.

||**Version 5**|**Version 4**|**Version 3**|**Test / Testp**|**niji**|
| :-: | :-: | :-: | :-: | :-: | :-: |
|Stylize default|1|NA|.25|NA|NA|
|Stylize Range|.5–2|NA|-10000–10000|NA|NA|

prompt example: /imagine prompt flowers.jpg birthday cake --iw .5

mj\_iw-start.jpg ¬

Image Prompt

mj\_iw-0-50.png ¬

--iw .5

mj\_iw-0-75.png ¬

--iw .75

mj\_iw-1-00.png ¬

--iw 1

mj\_iw-1-25.png ¬

--iw 1.25

mj\_iw-1-50.png ¬

--iw 1.5

mj\_iw-1-75.png ¬

--iw 1.75

mj\_iw-2-00.png ¬

--iw 2

