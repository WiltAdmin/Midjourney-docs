🌱 --seeds in Midjourney

What is a --seed?

"MJ uses a seed # to create a field of visual noise, like television static, as a starting point to generate the initial image grids. Seed #'s are generated randomly for each image but can be specified by adding the --seed parameter at the end of your prompt."

https://twitter.com/nickfloats/status/1632865293667295232
https://twitter.com/nickfloats/status/1632865313879621632
---

Why are --seeds useful in MJ?

Using the same prompt + seed in MJ v4 (the current default) will produce identical images.

This is VERY useful when building a prompt, b/c it lets you visualize the impact of any addition/change you make (like here, with lighting)

* Street style photo, a young brunette woman, standing, natural lighting, shot on fujifilm --ar 16:9 --seed 100
* Street style photo, a young brunette woman, standing, studio lighting, shot on fujifilm --ar 16:9 --seed 100
* Street style photo, a young brunette woman, standing, low-key lighting, shot on fujifilm --ar 16:9 --seed 100
* Street style photo, a young brunette woman, standing, neon lighting, shot on fujifilm --ar 16:9 --seed 100

https://twitter.com/nickfloats/status/1632865360260259840
---
Where can I find an images --seed in Midjourney?

You can:
-React w/ an envelope emoji to any job in Discord
-From MJ dashboard click image > ... > copy > seed
-Or specify yourself by adding --seed 12345 (or any # you'd like) at the end of your prompt.

https://twitter.com/nickfloats/status/1632865419458666498
---
Important note on --seed #'s in Midjourney

The --seed values only influence the initial image grid. This means if you upscale and image, the upscaled image will have a different seed than the initial image grid. The same goes for variations. I tend to use the initial seed.

https://twitter.com/nickfloats/status/1632865425179435017

### When/how to use --seed # in Midjourney (1/3)

1) Creating a consistent character
It starts with a model, and it seems to work best with a head and shoulders portrait photo like this one.

* 1960s street style photo of a young woman, latina, dior, silk, diamonds, dress, wide shot, natural lighting, soho, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622

https://twitter.com/nickfloats/status/1627157305040027648
---

Once you have your model, make sure you have the --seed for the image you're going to use. You can either add --seed 12345 (or any number you'd like) at the end of your prompt while iterating, or you can react to the image u want to use with the :envelope: emoji to find the seed

https://twitter.com/nickfloats/status/1627157306365411329
---

Next, copy the image URL and start a new prompt. In your prompt, include the URL, and the same prompt + seed you used to generate the image. Like this

* [URL] 1960s street style photo of a young woman, latina, dior, silk, diamonds, dress [...] --ar 16:9 --seed 1622

https://twitter.com/nickfloats/status/1627157307510386691
---
You should already start seeing some interesting variations. 

Now, try changing up some of the variables. Here i added "sitting" to the prompt.

* https://s.mj.run/YuSa9350SyA 1960s street style photo of a young woman, sitting, latina, dior, silk, diamonds, natural lighting, soho, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622

https://twitter.com/nickfloats/status/1627157309108506626
---
Here I changed the location to "Central Park"

* https://s.mj.run/YuSa9350SyA 1960s street style photo of a young woman, sitting, park bench, latina, dior, silk, diamonds, natural lighting, central park, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622 

https://twitter.com/nickfloats/status/1627157311050465281
---
Here we went to the beach

* https://s.mj.run/YuSa9350SyA 1960s street style photo of a young woman, walking, latina, dior, silk, diamonds, natural lighting, beach, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622 

https://twitter.com/nickfloats/status/1627157313160183809
---
And let's finish with a nice sunset at the beach

* https://s.mj.run/YuSa9350SyA 1960s beach style photo of a young woman, sitting, latina, dior, silk, diamonds, side view, side angle shot, sunset, beach, shot on Agfa Vista 200, 4k --ar 16:9 --seed 1622

https://twitter.com/nickfloats/status/1627157315387367426
---
Feel free to remix this and reply with some of your best side by sides. Have fun, and lmk if you have any questions. 
I'll be going into this in more depth on Youtube, and pushing the limits of this technique as much as I can.

https://twitter.com/nickfloats/status/1627157317308260358
---
Some notes: 

-I've found models that have a more unique/distinct look are more likely to result in consistent results.  

-keeping the variables similar to the prompt used to generate the original image helps

-you don't have to use the same seed, but i find it helps

https://twitter.com/nickfloats/status/1627160566912483329
---
more notes:

-try changing clothing, camera perspective, lighting, or location 

-try using variations with remix mode turned OFF. I find remix mode results in more drastic changes, while regular variations are great for creating unique changes in things like clothing

https://twitter.com/nickfloats/status/1627160568141430785
---

When/how to use --seed # in Midjourney (2/3)
2) Use --seeds to visualize the impact of changes to variables in your prompt. In these images, I used the same prompt + seed, but I changed the "LOCATION" in each.

* Street style photo, medium-full centered shot, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, afternoon, central park, shot on fujifilm --ar 16:9 --seed 100

* Street style photo, medium-full centered shot, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, afternoon, the beach, shot on fujifilm --ar 16:9 --seed 100

* Street style photo, medium-full centered shot, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, afternoon, paris, shot on fujifilm --ar 16:9 --seed 100

* Street style photo, medium-full centered shot, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, afternoon, coffee shop, shot on fujifilm --ar 16:9 --seed 100

https://twitter.com/nickfloats/status/1632865469987209216
---
When/how to use --seed # in Midjourney (2.5/3)
2.5) Use --seeds to visualize the impact of changes to variables in your prompt. In these images, I used the same prompt + seed, but I changed the "COLOR" in each.

* Editorial Style Photo, Eye Level, Coastal Bathroom, Clawfoot Tub, Seashell, Wicker, Mosaic Tile, Blue and White, Serena & Lily, Natural Light, Beach House, Afternoon, Relaxing, Coastal, Beachy, Nautical, 4k --ar 16:9 --seed 100

* Editorial Style Photo, Eye Level, Coastal Bathroom, Clawfoot Tub, Seashell, Wicker, Mosaic Tile, Orange and White, Serena & Lily, Natural Light, Beach House, Afternoon, Relaxing, Coastal, Beachy, Nautical, 4k --ar 16:9 --seed 100

* Editorial Style Photo, Eye Level, Coastal Bathroom, Clawfoot Tub, Seashell, Wicker, Mosaic Tile, Yellow and White, Serena & Lily, Natural Light, Beach House, Afternoon, Relaxing, Coastal, Beachy, Nautical, 4k --ar 16:9 --seed 100

* Editorial Style Photo, Eye Level, Coastal Bathroom, Clawfoot Tub, Seashell, Wicker, Mosaic Tile, Pink and White, Serena & Lily, Natural Light, Beach House, Afternoon, Relaxing, Coastal, Beachy, Nautical, 4k --ar 16:9 --seed 100

https://twitter.com/nickfloats/status/1632865513499164672
---
When/how to use --seed # in Midjourney (3/3)
3) Use --seeds to test the impact of syntax (i.e. the order of words) on your image generations. In these images, I used the same prompt + seed, but I moved the "Medium-full centered shot" variable to different areas.

* Medium-full centered shot, Street style photo, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, central park, coffee shop, shot on fujifilm --ar 16:9 --seed 100

* Street style photo, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, central park, coffee shop, shot on fujifilm, medium-full centered shot --ar 16:9 --seed 100

* Street style photo, medium-full centered shot, a young brunette woman, standing, wearing a red gucci jacket, natural lighting, central park, coffee shop, shot on fujifilm --ar 16:9 --seed 100

* Street style photo, a young brunette woman, standing, wearing a red gucci jacket, Medium-full centered shot, natural lighting, central park, coffee shop, shot on fujifilm --ar 16:9 --seed 100

https://twitter.com/nickfloats/status/1632865555903582208
---
