import openai

openai.api_key = "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"

completion = openai.ChatCompletion.create(
  model = "gpt-3.5-turbo",
  temperature = 0.8, #degree of randomness between 0 and 2
  max_tokens = 2000,
  messages = [
    {"role": "system", "content": "You are a story teller."},
    {"role": "user", "content": "Write the first chapter in a story on how rory goes about proposing to talia in a village without talia accepting yet"},
    {"role": "assistant", "content": "Rory confesses exuberantly, \"I want to spend the rest of my life with you!\""},
  ]
)

print(completion.choices[0].message)

#output
'''
{
  "role": "assistant",
  "content": "Chapter 1: The Heart's Desire\n\nIn the small, picturesque village of Briarwood, nestled amidst rolling hills and lush meadows, there 
lived a young man named Rory. With his warm, hazel eyes and a mischievous smile, Rory was well-known for his adventurous spirit and kind heart. But 
there was one thing that filled his mind day and night, consuming his every thought - the desire to propose to his beloved Talia.\n\nTalia, a vibrant and free-spirited woman, had captured Rory's heart from the moment they first met. Her infectious laughter and gentle demeanor made her the center of attention wherever she went. They had been together for many blissful years, their love growing stronger, but the time had come for Rory to take the next step.\n\nIt was a crisp autumn morning when Rory woke up with an overwhelming determination in his heart. He knew he had to propose to Talia, but he also knew that she was a woman with an independent spirit, unafraid to wander the world. This left him with a lingering uncertainty - would she be ready for the commitment he longed for?\n\nAs the sun began to rise, casting a golden glow across the village, Rory decided to seek the advice of the village's wise elder, known simply as Gramma Eliza. She was renowned for her wisdom and guidance, and it was said that she possessed a deep understanding of matters of the heart.\n\nWith a nervous excitement, Rory made his way to Gramma Eliza's cottage, which stood at the edge of the village, surrounded by vibrant wildflowers. The air was filled with the sweet scent of blooming roses as he knocked on the aged wooden door.\n\nGramma Eliza opened the door, her silver hair cascading down her back, and her eyes twinkling with a knowing gleam. \"Ah, young Rory,\" she greeted him warmly. \"I have been expecting you.\"\n\nRory was taken aback by her words. \"You have?\"\n\nWith a gentle smile, Gramma Eliza nodded. \"Love has 
a way of finding its way to my doorstep. It whispers its secrets in the wind, and today, it brought you here.\"\n\nFeeling a newfound sense of hope, Rory poured out his heart to the wise elder. He shared his fears of Talia's possible reluctance and his desire to propose, despite the uncertainty 
that loomed over him. Gramma Eliza listened intently, her eyes filled with compassion.\n\n\"My dear boy,\" she began, her voice melodic and soothing. \"Love is a vast and complex tapestry, woven with threads of joy, fear, and uncertainty. It is both a leap of faith and an act of vulnerability. But it is worth every moment of doubt.\"\n\nRory nodded, absorbing her words, feeling his determination strengthen. \"But what if Talia isn't ready? 
What if I propose, and she says no?\"\n\nGramma Eliza's wise eyes twinkled as she placed a comforting hand on Rory's shoulder. \"That is the risk we all take when we open our hearts to another. But remember, young Rory, the greatest journeys begin with a single step. Even if she does not accept 
right away, you will have spoken the truth of your heart, and that alone is a gift.\"\n\nFeeling a renewed sense of clarity and purpose, Rory thanked Gramma Eliza for her guidance and made his way back to the heart of the village. As he walked along the cobblestone streets, he couldn't help but 
feel a mixture of nervousness and excitement tugging at his core.\n\nRory knew that proposing to Talia was not a decision to be taken lightly. It was a leap of faith, a declaration of his unwavering love, and a testament to their shared future. Despite the uncertainty that lay before him, he was determined to take that step, to offer Talia his heart and his dreams.\n\nAnd so, with each step he took, Rory's heart raced with anticipation, knowing that the path to Talia's acceptance might be uncertain, but his love for her was unwavering. The stage was set, and the tale of Rory's proposal was about to unfold, forever altering the course of their lives."
}

{
  "role": "assistant",
  "content": "Chapter 1: The Heart's Desire
  
  In the small, picturesque village of Briarwood, nestled amidst rolling hills and lush meadows, there 
lived a young man named Rory. With his warm, hazel eyes and a mischievous smile, Rory was well-known for his adventurous spirit and kind heart. But 
there was one thing that filled his mind day and night, consuming his every thought - the desire to propose to his beloved Talia.

Talia, a vibrant and free-spirited woman, had captured Rory's heart from the moment they first met. Her infectious laughter and gentle demeanor made her the center of attention wherever she went. 
They had been together for many blissful years, their love growing stronger, but the time had come for Rory to take the next step.
It was a crisp autumn morning when Rory woke up with an overwhelming determination in his heart. He knew he had to propose to Talia, but he also knew that she was a woman with an independent spirit, 
unafraid to wander the world. This left him with a lingering uncertainty - would she be ready for the commitment he longed for?
As the sun began to rise, casting a golden glow across the village, Rory decided to seek the advice of the village's wise elder, known simply as Gramma Eliza. 
She was renowned for her wisdom and guidance, and it was said that she possessed a deep understanding of matters of the heart.

With a nervous excitement, Rory made his way to Gramma Eliza's cottage, which stood at the edge of the village, surrounded by vibrant wildflowers. 
The air was filled with the sweet scent of blooming roses as he knocked on the aged wooden door.

Gramma Eliza opened the door, her silver hair cascading down her back, and her eyes twinkling with a knowing gleam. "Ah, young Rory," she greeted him warmly. "I have been expecting you."

Rory was taken aback by her words. "You have?" 

With a gentle smile, Gramma Eliza nodded. "Love has a way of finding its way to my doorstep. It whispers its secrets in the wind, and today, it brought you here."

Feeling a newfound sense of hope, Rory poured out his heart to the wise elder. He shared his fears of Talia's possible reluctance and his desire to propose, despite the uncertainty 
that loomed over him. Gramma Eliza listened intently, her eyes filled with compassion. "My dear boy," she began, her voice melodic and soothing. 
"Love is a vast and complex tapestry, woven with threads of joy, fear, and uncertainty. It is both a leap of faith and an act of vulnerability. But it is worth every moment of doubt."

Rory nodded, absorbing her words, feeling his determination strengthen. "But what if Talia isn't ready? What if I propose, and she says no?"

Gramma Eliza's wise eyes twinkled as she placed a comforting hand on Rory's shoulder. "That is the risk we all take when we open our hearts to another. But remember, young Rory, 
the greatest journeys begin with a single step. Even if she does not accept right away, you will have spoken the truth of your heart, and that alone is a gift."

Feeling a renewed sense of clarity and purpose, Rory thanked Gramma Eliza for her guidance and made his way back to the heart of the village. As he walked along the cobblestone streets, he couldn't help but 
feel a mixture of nervousness and excitement tugging at his core.\n\nRory knew that proposing to Talia was not a decision to be taken lightly. 
It was a leap of faith, a declaration of his unwavering love, and a testament to their shared future. Despite the uncertainty that lay before him, he was determined to take that step, 
to offer Talia his heart and his dreams.\n\nAnd so, with each step he took, Rory's heart raced with anticipation, 
knowing that the path to Talia's acceptance might be uncertain, but his love for her was unwavering. The stage was set, and the tale of Rory's proposal was about to unfold, 
forever altering the course of their lives."
}
'''
