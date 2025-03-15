print("Welcome to KBC!")
questions = [
    ["1. Which Programming Language was used to create Facebook?", "Python", "HTML", "JavaScript", "PHP", "C++", 4],

    ["2. When is Windows 10 end of support by Microsoft?", "2026-Nov", "2055-Jun", "2025-Oct", "2034-May", "2024-Dec", 3],

    ["3. Which one is not a web browser?", "Chrome", "Linux", "Safari", "Firefox", "Edge", 2],

    ["4. What is HTTP used for?", "Email", "Gaming", "Coding", "Browsing", "Calling", 4],

    ["5. Which is a social media platform?", "Facebook", "Python", "ChatGPT", "Excel", "Capcut", 1],

    ["6. Which company owns YouTube?", "Meta", "Apple", "Google", "Microsoft", "Amazon", 3],

    ["7. What does VPN protect?", "Ads", "Privacy", "Speed", "Viruses", "User", 2],

    ["8. Which is a search engine?", "Bing", "WhatsApp", "Photoshop", "Discord", "Copilot", 1],

    ["9. What does a Firewall do?", "Boost Speed", "Delete Files", "Block Access", "Open Sites", "Burn Data", 3],

    ["10. What is 'www' short for?", "World Wide Web", "Web World Wibe", "Wonder Wide Web", "World Wide Well", "Wonderful World's Web", 1],

    ["11. Which Keyboard Key is used to Refresh?", "Ctrl", "R", "Esc", "F5", "/", 4],

    ["12. Which device connects to Wi-Fi?", "CPU", "Router", "Printer", "DVD", "TV", 2],

    ["13. What is 'Google' known as?", "Search Engine", "Social Media", "Operating System", "Chatbot", "Photo Editor", 1],

    ["14. Which is a File type for Images?", "PDF", "TXT", "JPG", "MP4", "EXE", 3],

    ["15. What is 'Ctrl + X' used for?", "Copy", "Cut", "Paste", "Undo", "Redo", 2],

    ["16. What is YouTube used for?", "Video Sharing", "Search Engine", "Code Editor", "Video Editor", 1],
]

levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
  
  question = questions[i]
  print(f"\n\nQuestion for Rs. {levels[i]}")
  print(f"a. {question[1]}          b. {question[2]} ")
  print(f"c. {question[3]}          d. {question[4]} ")
  print(f"e.{question[5]}")
  reply = int(input("Enter your answer (1-5) or  0 to quit:\n" ))
  if (reply == 0):
    money = levels[i-1]
    break
  if(reply == question[-1]):
    print(f"Correct answer, you have won Rs. {levels[i]}")
    if(i == 4):
      money = 10000
    elif(i == 9):
      money = 320000
    elif(i == 14):
      money = 10000000
  else:
    print("Wrong answer!")
    break 

print(f"Your take home money is {money}")