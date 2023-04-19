**Fast and Relax Modes**

**Midjourney uses powerful Graphics Processing Units (GPUs) to interpret and process each prompt. When you purchase a subscription to Midjourney, you are purchasing time on these GPUs.**

Different [subscription plans](https://docs.midjourney.com/plans) have different amounts of monthly GPU time.This monthly subscription GPU time is **Fast Mode** time. Fast Mode tries to give you a GPU instantly. It's the highest-priority processing tier and uses your subscription's monthly GPU time.

Run Out of Time?

You can purchase more Fast Hours on your [Midjourney.com/accounts](https://www.midjourney.com/account/) page.

**How many GPU minutes do my generations cost?**

The Average Job the Midjourney bot processes takes about one minute of GPU time to finish creating an image. Upscaling an image or using nonstandard aspect ratios may take more time. Creating variations or using lower quality values will take less time.

A Job's cost depends on the following factors:

||**+ Lower Cost**|**++ Average Cost**|**+++ Higher Cost**|
| :-: | :-: | :-: | :-: |
|Job Type|Variations|/imagine|Upscale|
|Aspect Ratio||default (square)|tall or wide|
|Model Version||default (--v 4)|--test or --testp|
|Quality Parameter|--q 0.25 or --q 0.5|default (--q 1)|--q 2|
|Stop Parameter|--stop 10–--stop 99|default (--stop 100)||

Use /info before and after running a process to see how many of your remaining GPU minutes the generation used.


**Fast vs. Relax Mode**

Subscribers to the Standard and Pro plans can create an unlimited number of images each month in Relax Mode. Relax Mode will not cost any of your GPU time, but Jobs will be placed into a queue based on how much you've used the system.

**How long do I need to wait in Relax mode?**

Jobs in Relax mode are placed in a queue to be processed as GPUs become available. Wait times for Relax are dynamic but generally range between 0–10 minutes per job. If you use Relax mode occasionally, you will have shorter wait times compared to subscribers that have used it more. This priority currently resets whenever you renew your monthly subscription.

Note!

By default, images are generated using Fast Mode.When your subscription resets each month, you are automatically switched to Fast Mode.

**How to Switch Between Modes**

**Use the /fast or /relax command**

Standard and Pro plan subscribers can use the /fast or /relax commands to switch between modes.MJ\_FastCommand.gif ¬

**Use the Settings Command**

Use the [/settings command ](https://docs.midjourney.com/settings-and-presets)and choose 🐇 Fast or 🐢 Relax from the menu.
