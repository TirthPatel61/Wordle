from letter_state import LetterState

class Wordle:
    MAX_ATTEMPTS = 6
    WORD_LENGTH = 5
    
    def __init__(self, secret: str):
        self.secret = secret.upper()
        self.attempts = []

    def attempt(self, word: str):
        word = word.upper()
        self.attempts.append(word)
    
    def gameWin(self):
        return len(self.attempts) > 0 and self.attempts[-1] == self.secret
    
    def remainingAttempts(self):
        return self.MAX_ATTEMPTS - len(self.attempts)
    
    def stillAttempt(self):
        return self.remainingAttempts() > 0 and not self.gameWin()
    
    def guess(self, word: str):
        word = word.upper()
        remaining_secret = list(self.secret)
        result = []
        for char in word:
            result.append(LetterState(char))
        for i in range(self.WORD_LENGTH):
            letter = result[i]
            if letter.character == remaining_secret[i]:
                letter.in_right_position = True
                remaining_secret[i] = '*'
        
        for i in range(self.WORD_LENGTH):
            letter = result[i]

            if letter.in_right_position:
                continue
            
            for j in range(self.WORD_LENGTH):
                if letter.character == remaining_secret[j]:
                    remaining_secret[j] = "*"
                    letter.in_word = True
                    break
        return result