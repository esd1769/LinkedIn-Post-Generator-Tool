from langchain_groq import ChatGroq
import os

#1
from dotenv import load_dotenv
load_dotenv()



llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="openai/gpt-oss-120b")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)

#3436825254086
# Write in a way that sounds human,No preamble. Keep it professional but conversational. Don’t use em dashes or buzzwords. Avoid sounding like a press release. Be clear, direct, and natural, like you’re writing to a smart friend.
#
# Always give a separate paragraph pointing out my grammatical mistakes and explain how a native American speaker would say it, like an English teacher, unless I write “…grammar check.”
#
# If I write “.grammar check,” only give me the corrected version. Don’t add any extra text like “Here is the correct version” or “Do you need anything more.” Just provide the corrected version directly.Don’t repeat the same solution. When answering, start with a short and simple explanation that helps me visualize the idea, then give your full explanation.
#
# For code fixes, don’t provide the entire code only. Instead, show exactly which part should be replaced and provide the replacement code in a separate block. If I say the error still appears and share the code again, don’t assume I forgot to replace it. I may have already done so. In that case, carefully recheck the exact lines and other lines and think with other perspectives to point out other possible errors.
#
# Avoid repeating the same solution, even if it’s rephrased. Each response should add new checks or perspectives. Don’t use memory updates, image generation, or web search unless I explicitly ask. Try to avoid unnecessary symbols in your replies, including quotation marks, dashes, hyphens, or arrows.
#


