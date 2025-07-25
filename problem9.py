# replace the words

letter = ''' 
            Dear <|Name|>,
            You are selected!
            <|Date|>.
        '''
print(letter.replace("<|Name|>", "Tushar").replace("<|Date|>", "28th July, 2025"))
