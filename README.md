an Ugly Trivia Game

This game needs refactoring!

Two things to consider:
1. Testing with Golden Master

We can’t write reasonable unit tests without refactorings first. But we don’t want to refactor without tests at all.

But we can test the application as a whole. Gain control over all external input sources (RNGs, system time, keyboard input and so on). Then save all outputs produced (console output, emails sent, files changed etc). This is our Golden Master.

Now we can change the code and compare if it still yields the same results as before.

2. Using Tools - Free Fall

This is another thing to try out. And probably it’s a good idea to not learn this in production. Just use your IDE refactorings. Do not waste time to understand the code. Trust your IDE and use features like extract method or invert if statement. You will be surprised about the results.

----------------------------------------------------------------------------------------------------
Explanation:
The game needs atleast 2 players. The first player to get 6 gold coins wins. You gain a gold coin everytime the player gets a question right. The players names are saved and a list of 50 fake questions are added with what number question they are. When it is a player's turn, the category is decided by what number square you are on. The question is chosen from that category and a die is rolled to decide if you are correct or not. If you are correct, you gain a gold coin. If you are incorrect, you get send to the penalty box. Everytime it is your turn, you have a chance to get out of the penalty box by rolling an even number.