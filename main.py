import re
import sys
with open('./words.txt', 'r') as f:
    words = f.read()

class TreeDSNode:
    def __init__(self, word, used_words:list):
        self.word = word
        self.used_words = used_words
        self.children = []
    
    def add_child(self, child):
        self.children.append(child)
    
    def add_used_word(self, word):
        self.used_words.append(word)
    
    def get_used_words(self):
        return self.used_words
    
    def get_children(self):
        return self.children

def get_similar_words(word):
    found_words = []
    # find word in words by removing one character at a time
    for i in range(len(word)):
        pattern = '\n'+word[:i]+'[a-z]?'+word[i+1:]+'\n'
        matches = re.findall(pattern, words)
        if len(matches) > 0:
            found_words.extend(matches)
        
    for i in range(len(word) + 1):
        pattern = '\n'+word[:i]+'[a-z]?'+word[i:]+'\n'
        matches = re.findall(pattern, words)
        if len(matches) > 0:
            found_words.extend(matches)

    # set
    found_words = list(set(found_words))
    found_words = [word.strip() for word in found_words]
    return found_words

def traverse_tree(node:TreeDSNode, target, all_used_words):
    if node.word == target:
        print(node.used_words)
        print('\n')
        return

    if len(node.get_used_words()) > 20:
        return
    
    # get children
    children = node.get_children()
    if len(children) == 0:
        similar_words = get_similar_words(node.word)
        for word in similar_words:
            if word not in all_used_words:
                all_used_words.append(word)
                child_node = TreeDSNode(word, node.get_used_words() + [word])
                node.add_child(child_node)
                traverse_tree(child_node, target, all_used_words)
    

def main():
    if len(sys.argv) != 3:
        print('Usage: ./main.py <word> <target>')
        sys.exit(1)

    word = sys.argv[1]
    target = sys.argv[2]
    similar_words = get_similar_words(word)
    all_used_words = [word]
    parent_node = TreeDSNode(word, [word])
    traverse_tree(parent_node, target, all_used_words)

if __name__ == '__main__':
    main()