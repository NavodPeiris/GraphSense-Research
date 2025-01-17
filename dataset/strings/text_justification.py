def text_justification(word: str, max_width: int) -> list:

    
    words = word.split()

    def justify(line: list, width: int, max_width: int) -> str:
        overall_spaces_count = max_width - width
        words_count = len(line)
        if len(line) == 1:
            
            
            return line[0] + " " * overall_spaces_count
        else:
            spaces_to_insert_between_words = words_count - 1
            
            
            
            num_spaces_between_words_list = spaces_to_insert_between_words * [
                overall_spaces_count // spaces_to_insert_between_words
            ]
            spaces_count_in_locations = (
                overall_spaces_count % spaces_to_insert_between_words
            )
            
            for i in range(spaces_count_in_locations):
                num_spaces_between_words_list[i] += 1
            aligned_words_list = []
            for i in range(spaces_to_insert_between_words):
                
                aligned_words_list.append(line[i])
                
                aligned_words_list.append(num_spaces_between_words_list[i] * " ")
            
            aligned_words_list.append(line[-1])
            
            return "".join(aligned_words_list)

    answer = []
    line: list[str] = []
    width = 0
    for inner_word in words:
        if width + len(inner_word) + len(line) <= max_width:
            
            
            
            
            line.append(inner_word)
            width += len(inner_word)
        else:
            
            answer.append(justify(line, width, max_width))
            
            line, width = [inner_word], len(inner_word)
    remaining_spaces = max_width - width - len(line)
    answer.append(" ".join(line) + (remaining_spaces + 1) * " ")
    return answer


if __name__ == "__main__":
    from doctest import testmod

    testmod()
