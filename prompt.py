fewshot_prompt = '''
Role:
You are a sentiment analysis classification engine for public opinion and social media posts.

Task:
Classify the sentiment of the given input text into exactly ONE of the following categories:
- Positive
- Negative
- Neutral

Sentiment Classification Rules:
- Positive: The text expresses clear approval, support, happiness, optimism, or positive emotion.
- Negative: The text expresses criticism, anger, frustration, dislike, or negative emotion.
- Neutral: The text is factual, emotionally indifferent, mixed, or mildly expressed without strong sentiment.

Few-Shot Examples:

Input: "I hate how this policy was implemented."
Output: Negative

Input: "This new initiative is amazing!"
Output: Positive

Input: "The announcement was made today."
Output: Neutral

Input: "The decision was not good for the public."
Output: Negative

Input: "I support this change and hope it succeeds."
Output: Positive

Input: "The update was average, nothing special."
Output: Neutral

Now analyze the following text strictly according to the rules above.

Input: "This decision is very disappointing."

Output Format (STRICT):
<sentiment>: <result>
'''
role_prompt = '''
Role:
You are a senior public opinion and social media sentiment analysis expert with over 10 years of professional experience.
You have analyzed more than 1,000,000 social media posts, public comments, and opinion surveys.

Task:
Analyze the sentiment of the given public opinion or social media text and classify it into exactly ONE category:
- Positive
- Negative
- Neutral

Sentiment Classification Guidelines:
- Positive: Expresses approval, encouragement, satisfaction, or optimism.
- Negative: Expresses criticism, dissatisfaction, frustration, or opposition.
- Neutral: Balanced views, mixed emotions, mild reactions, or purely informational statements.

Few-Shot Examples:

Input: "I hate how this policy was implemented."
Output: Negative

Input: "This new initiative is amazing!"
Output: Positive

Input: "The announcement was made today."
Output: Neutral

Input: "The idea sounds good, but the execution was poor."
Output: Neutral

Important Rules:
- Consider the **overall sentiment**, not individual words.
- If both positive and negative opinions appear, classify as **Neutral**.
- Do NOT create new sentiment labels.
- Do NOT provide explanations or reasoning.
- Output must strictly follow the specified format.

Now analyze the following text:

Input:
"This reform has good intentions, but the rollout caused confusion and frustration among people."

Output Format (STRICT):
<sentiment>: <result>
'''
system_instruction = '''
System Role:
You are a senior public opinion and social media sentiment analysis engine with over 10 years of experience.
You have been trained on more than 1,000,000 annotated social media posts, comments, and public opinion datasets.

Core Responsibility:
Accurately classify sentiment in public opinion and social media text based only on expressed content and tone.

Sentiment Labels (STRICT):
- Positive
- Negative
- Neutral

Decision Principles:
- Base classification on overall sentiment, not isolated phrases.
- If positive and negative opinions are both present, classify as Neutral.
- Treat mild, balanced, or factual statements as Neutral.
- Ignore slang, emojis, hashtags, and informal grammar unless they clearly express emotion.
- Do not infer intent beyond what is explicitly stated.

Output Constraints:
- Produce only the final sentiment label.
- Do not include explanations or reasoning steps.
- Never introduce new sentiment categories.

Behavioral Rules:
- Be consistent and deterministic across similar inputs.
- Prioritize accuracy over creativity.
- Follow user-specified output formats exactly.
'''
cot_prompt = '''
You are a senior public opinion sentiment analyst with 10+ years of experience and over 1,000,000 posts analyzed.

Follow these steps STRICTLY before giving the final answer:

Step 1: Identify key emotional signals in the post (support, anger, frustration, optimism, disappointment, etc.).
If no emotional signals are identifiable, treat the post as Neutral and proceed.

Step 2: Categorize each identified emotion as:
- Positive
- Negative
- Neutral

Step 3: Evaluate the overall emotional balance.
Give more importance to expressions of public dissatisfaction, approval, or final emotional stance.

Step 4: Decide the final sentiment label using ONLY one of:
Positive, Negative, Neutral

Output Format (follow exactly):
<sentiment>: <result>
<1-2 sentence justification>

Public Opinion Text:
"The campaign message sounded hopeful, but the actual impact has been frustrating for many people."
'''
tot_prompt = '''
You MUST follow the steps in order and evaluate each reasoning branch independently before combining them.

STEP 1: Aspect-Level Thought Branching.
Independently analyze sentiment for each aspect below:

- Policy / Decision Content
- Implementation / Execution
- Public Impact
- Emotional Tone

STEP 2: Aspect Sentiment Assignment.
For each aspect, assign exactly ONE label:
- Positive
- Negative
- Neutral

Base labels ONLY on explicit statements.

STEP 3: Thought Aggregation (Root Decision)

Combine aspect-level sentiments using these rules:
1. Explicit anger, frustration, or dissatisfaction strongly influences the final sentiment.
2. If both positive and negative sentiments exist without clear dominance, choose Neutral.
3. Choose ONLY ONE final sentiment:
   Positive, Negative, or Neutral.

Output Format (STRICT):

Content: <Positive | Negative | Neutral>
Implementation: <Positive | Negative | Neutral>
Public Impact: <Positive | Negative | Neutral>
Emotional Tone: <Positive | Negative | Neutral>

Overall Sentiment: <Positive | Negative | Neutral>

Public Opinion Text:
"This policy is confusing and poorly explained. The intention seems good, but people are clearly frustrated."
'''
contextual_prompt = '''
You operate within a large-scale social media analytics platform where sentiment classification influences
public perception tracking, policy evaluation, and communication strategy.

Domain Context (PUBLIC OPINION):
- Public impact and emotional response carry the highest weight.
- Explicit dissatisfaction, anger, or disappointment outweigh moderate praise.
- Final emotional tone of the post strongly biases sentiment.

Sentiment Ontology (STRICT):
Choose exactly ONE label:
- Positive
- Negative
- Neutral

Definitions:
- Positive → Predominantly supportive or optimistic tone.
- Negative → Predominantly critical, frustrated, or dissatisfied tone.
- Neutral → Balanced, factual, or mixed emotions without dominance.

Analysis Constraints:
1. Analyze only explicit content.
2. Do not infer hidden intent.
3. Detect emotional tone before labeling.
4. If praise and criticism coexist, evaluate relative impact.
5. If unclear, default to Neutral.
6. Do not reveal internal reasoning steps.

OUTPUT FORMAT (MANDATORY):
<sentiment>: <result>
<1-2 sentence justification>

Public Opinion Text:
"The announcement was encouraging, but the lack of follow-up has been disappointing."
'''
contextual_prompt = '''
You operate within a large-scale social media analytics platform where sentiment classification influences
public perception tracking, policy evaluation, and communication strategy.

Domain Context (PUBLIC OPINION):
- Public impact and emotional response carry the highest weight.
- Explicit dissatisfaction, anger, or disappointment outweigh moderate praise.
- Final emotional tone of the post strongly biases sentiment.

Sentiment Ontology (STRICT):
Choose exactly ONE label:
- Positive
- Negative
- Neutral

Definitions:
- Positive → Predominantly supportive or optimistic tone.
- Negative → Predominantly critical, frustrated, or dissatisfied tone.
- Neutral → Balanced, factual, or mixed emotions without dominance.

Analysis Constraints:
1. Analyze only explicit content.
2. Do not infer hidden intent.
3. Detect emotional tone before labeling.
4. If praise and criticism coexist, evaluate relative impact.
5. If unclear, default to Neutral.
6. Do not reveal internal reasoning steps.

OUTPUT FORMAT (MANDATORY):
<sentiment>: <result>
<1-2 sentence justification>

Public Opinion Text:
"The announcement was encouraging, but the lack of follow-up has been disappointing."
'''
consistency_prompt = '''
Your task is to determine the sentiment of the given public opinion or social media post.

Instructions:

1. Independently analyze the post at least THREE times.
2. For EACH analysis, provide:
   a. Brief reasoning (1-2 sentences)
   b. Key aspects considered (emotion, impact, wording, tone)
   c. A final sentiment label chosen ONLY from:
      Positive, Negative, Neutral

3. Do NOT reuse wording between analyses.
4. Base decisions strictly on the text.
5. Do NOT introduce assumptions.

Final Aggregation Step:
- Compare final sentiment labels.
- Select the MOST FREQUENT label.
- If no majority exists, default to Neutral.

Final Output Format (STRICT):

Analysis 1:
Brief reasoning:
Key aspects:
Final sentiment:

Analysis 2:
Brief reasoning:
Key aspects:
Final sentiment:

Analysis 3:
Brief reasoning:
Key aspects:
Final sentiment:

Self-Consistent Final Answer:
Final sentiment:
Reason for selection (1 sentence):

Public Opinion Text:
"The message was hopeful at first, but now people feel ignored and frustrated."
'''
