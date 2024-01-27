from bardapi import Bard
import os , time
os.system('clear')
time.sleep(1)
print(((Bard(token = "fwilwx1fjOC0z04elgwEaJiQzLdSjuj2k04L3SH06M2_XZBmfLd43gdLGDIj6R21eCW0ig.")).get_answer(f'Give a hint for the answer to the question in one line {input("What is your query: ")}. Do not give the answer.'))["content"])