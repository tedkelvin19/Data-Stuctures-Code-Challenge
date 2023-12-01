# Question 1 Solution.

def is_balanced(expression):
        stack = []
        opening_chars = ["(", "{", "["]
        closing_chars = [")", "}", "]"]
        for char in expression:
            if char in opening_chars:
                stack.append(char)
            elif char in closing_chars:
                if not stack:
                    return False
                top_char = stack.pop()
                if opening_chars.index(top_char) != closing_chars.index(char):
                    return False
        return len(stack) == 0

expression1 = "([]{})()"
expression2 = "()[(]]{}"

print(is_balanced(expression1))
print(is_balanced(expression2))


# Question 2 Solution.

def remove_duplicates(sequence):
    seen = set()
    result = []
    for item in sequence:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

list1= [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(remove_duplicates(list1))
print(list1)



# Question 3 Solution.

def word_frequency(sentence):
    frequency = {}
    words = sentence.split()
    for word in words:
        if word in frequency:
            frequency[word] += 1
        else:
            frequency[word] = 1
    return frequency

line1 = "Learning programming is very exiciting. I love it. programming in python is very exiciting." 
print(word_frequency(line1))