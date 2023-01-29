# while loop
i = 1
while i <= 10:
    print(i)
    i += 1

print("Done with loop.")

# building a guessing game
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_guesses = False

while guess != secret_word and not(out_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ")
        guess_count += 1
    else:
        out_guesses = True

if out_guesses:
    print("You lose")
else:
    print("You win")
