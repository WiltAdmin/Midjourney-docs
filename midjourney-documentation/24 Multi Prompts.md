**Multi Prompts**

**It is possible to have the Midjourney Bot consider two or more separate concepts individually using :: as a separator. Separating prompts allows you to assign relative importance to parts of a prompt.**

**Multi-Prompt Basics**

Adding a double colon :: to a prompt indicates to the Midjourney Bot that it should consider each part of the prompt separately. In the example below, for the prompt hot dog all words are considered together, and the Midjourney Bot produces images of tasty hotdogs. If the prompt is separated into two parts, hot:: dog both concepts are considered separately, creating a picture of a dog that is warm.

There is no space between the double colons ::Multi-prompts work with [Model Versions](https://docs.midjourney.com/models) 1, 2, 3, 4, '5, niji, and niji 5Any [parameters](https://docs.midjourney.com/parameter-list) are still added to the very end of the prompt.

**hot dog**

MJ\_Multi\_hotdog.jpg ¬

*Hot dog* is considered as a single thought.

**hot:: dog**

MJ\_Multi\_hot-dog.jpg ¬

*Hot* and *dog* Hot and dog are considered separate thoughts

cup cake illustration

MJ\_Multi\_cupCakeIllustration.jpg ¬

*Cup cake illustration* is considered together producing illustrated images of cup cakes.

cup:: cake illustration

MJ\_Multi\_cup-cakeIllustration.jpg ¬

*Cup* is considered separately from *cake illustration* producing images of cakes in cups.

cup:: cake:: illustration

MJ\_Multi\_cup-cake-illustration.jpg ¬

*Cup*, *cake*, and *illustration* are considered separately, producing a cake in a cup with common illustration elements like flowers and butterflies.

**Prompt Weights**

When a double colon :: is used to separate a prompt into different parts, you can add a number immediately after the double colon to assign the relative importance to that part of the prompt.

In the example below, the prompt hot:: dog produced a dog that is hot. Changing the prompt to hot::2 dog makes the word **hot** twice as important as the word dog, producing an image of a dog that is *very hot!*

[Model Versions] 1, 2, 3 only accept whole numbers as weights[Model Versions] 4 can accept decimal places for weightsNon-specified weights default to 1.

**hot:: dog**

MJ\_Multi\_hot-dog.jpg ¬

*Hot* and *dog* are considered as separate thoughts

**hot::2 dog**

MJ\_Multi\_hot2-dog.jpg ¬

*Hot* is twice as important as *Dog*

**Weights are normalized:**hot:: dog is the same as hot::1 dog, hot:: dog::1,hot::2 dog::2, hot::100 dog::100, etc.cup::2 cake is the same as cup::4 cake::2, cup::100 cake::50 etc.cup:: cake:: illustration is the same as cup::1 cake::1 illustration::1, cup::1 cake:: illustration::, cup::2 cake::2 illustration::2 etc.

**Negative Prompt Weights**

Negative weights can be added to prompts to remove unwanted elements.The sum of all weights must be a positive number.

vibrant tulip fields

MJ\_Multi\_Tulips.jpg ¬

A range of colored tulips are produced.

vibrant tulip fields:: red::-.5

MJ\_Multi\_Tulips\_NoRed.jpg ¬

*Tulip fields are less likely to contain the color red.*

**Weights are normalized so:**tulips:: red::-.5 is the same as tulips::2 red::-1, tulips::200 red::-100, etc.

**The --no Parameter**

The --no [parameter](https://docs.midjourney.com/v1/docs/parameter-list) is the same as weighing part of a multi prompt to "-.5" vibrant tulip fields:: red::-.5 is the same as vibrant tulip fields --no red.
