def mood_tracker():
    days_to_track = 14
    overall_mood = []
    mood_scores = []

    while days_to_track > 0:
        days_to_track -= 1
        user_mood = input("What's your mood today? (☺️🥴😅😪😭🥲): ")
        mood_score = 0

        if user_mood == "☺️":
            print("I'm feeling good to hear that, you're so happy today.")
            mood_score = 10
            overall_mood.append("good")
        elif user_mood == "🥴":
            print("Wow, you look exactly like me now 😁. You're feeling crazy today.")
            mood_score = 5
            overall_mood.append("crazy")
        elif user_mood == "😅":
            print("Sorry to hear that🙁. You're a mystery to me, give me a clue to solve the mystery😌.")
            mood_score = 4
            overall_mood.append("uncertain")
        elif user_mood == "😪":
            print("You look funny 😂. Do you have a cold? 😆 Sorry, sorry, sorry, don't be angry with me😑.")
            mood_score = 5
            print("What did I do? 😑 You look beautiful when you feel that way 😬🙃. You're annoyed for some reason.")
            overall_mood.append("annoyed")
        elif user_mood == "😭":
            print("I'm feeling sad🥲 to hear that, you're crying now.")
            mood_score = 1
            overall_mood.append("crying")
        elif user_mood == "🥲":
            print("What happened to you? You're feeling sad today.")
            mood_score = 2
            overall_mood.append("sad")
        else:
            print("That's not a valid mood emoji. Please try again.")
            continue

        mood_scores.append(mood_score)

    print("\n---Happyness Meter ---")
    if mood_scores:
        average_mood_score = sum(mood_scores) / len(mood_scores)
        print(f"Your average mood score is: {average_mood_score:.2f}")

        if average_mood_score >= 8:
            print("Your estimated happiness level is: Very Happy! 😊")
        elif average_mood_score >= 5:
            print("Your estimated happiness level is: Good! 👍")
        elif average_mood_score >= 3:
            print("Your estimated happiness level is: Okay. 🙂")
        else:
            print("Your estimated happiness level is: Needs Improvement. 😞")
    else:
        print("No valid moods were entered.")

    
