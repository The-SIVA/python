sentenct_list = input().split()
length_of_sentence_list = len(sentenct_list)
sum_of_all_words_lengths = 0
for word in sentenct_list:
    length_of_word = len(word)
    sum_of_all_words_lengths += length_of_word

average_length_of_words_in_sentence = (sum_of_all_words_lengths/length_of_sentence_list)
print(average_length_of_words_in_sentence)