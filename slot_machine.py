import random
symbols = ['🍒',' 🍇', '🍉', '7️⃣']
results = [random.choice(symbols) for _ in range(3)]
print(" | ".join(results))
if results == ['7️⃣', '7️⃣', '7️⃣']:
    print("Jackpot! You win 100 coins!")
else:
    print("Better luck next time!") 
    
def play():
    while True:
        results = [random.choice(symbols) for _ in range(3)]
        print(" | ".join(results))
        if results == ['7️⃣', '7️⃣', '7️⃣']:
            print("Jackpot! You win 100 coins!")
        else:
            print("Better luck next time!") 
        again = input("Do you want to play again? (Y/N): ").strip().upper()
        if again != 'Y':
            print("Thanks for playing!")
            break
        play()
        
