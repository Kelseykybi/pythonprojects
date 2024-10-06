def sort_words_by_length(words):  
    return sorted(words, key=len)  

input_list = ["Mercedes", "Volkswagen", "Audi", "Hyundai", "Subaru"]  
sorted_words = sort_words_by_length(input_list)  
print(sorted_words)
