# The "distance" between two vectors is the angle between them.
# If x = (x1, x2, ..., xn) is the first vector (xi = freq of word i)
# and y = (y1, y2, ..., yn) is the second vector,
# then the angle between them is defined as:
#    d(x,y) = arccos(inner_product(x,y) / (norm(x)*norm(y)))
# where:
#    inner_product(x,y) = x1*y1 + x2*y2 + ... xn*yn
#    norm(x) = sqrt(inner_product(x,x))

import sys, math, string

def read_file(filename):
    try:
        f = open(filename, 'r')
        return f.read()
    except:
        print(f"Error opening file: ${filename}")
        exit()

table = str.maketrans( string.punctuation + string.ascii_uppercase,
                      " "*len(string.punctuation) + string.ascii_lowercase)

def count_words(lines):

    lines = lines.translate(table)
    words = lines.split()
    count = {}
    for word in words:
        if word in count:
            count[word] = count[word] + 1
        else:
            count[word] = 1 
    
    return count

def word_frequencies_for_file(filename):
    lines = read_file(filename)
    words_count = count_words(lines)
    print(f"{filename} #{len(lines)} lines")
    print(f"#{len(words_count)} unique words")

    return words_count

def dot_product(dict_1, dict_2):
    dot_product = 0
    for key, value in dict_1.items():
        if key in dict_2:
            dot_product+= value * dict_2[key]
    
    return dot_product

def vector_angle(dict_1, dict_2):
    numerator = dot_product(dict_1,dict_2)
    denominator = math.sqrt( dot_product(dict_1, dict_1) * dot_product(dict_2, dict_2))

    
    return math.acos(numerator / denominator)

def main():
    if len(sys.argv) != 3:
        print("Usage: docdist1.py filename_1 filename_2")
    else:
        filename_1 = sys.argv[1]
        filename_2 = sys.argv[2]
        sorted_word_list_1 = word_frequencies_for_file(filename_1)
        sorted_word_list_2 = word_frequencies_for_file(filename_2)
        distance = vector_angle(sorted_word_list_1,sorted_word_list_2)
        print("The distance between the documents is: %0.6f (radians)"%distance)

if __name__ == "__main__":
    import profile
    profile.run("main()")

#############################################################
#   ".\tests\Alice.txt" ".\tests\JFK.txt" = 0.895626
#   ".\tests\lewis.txt" ".\tests\Tom Sawyer.txt" = 0.565878
#       Benchmarks:             MINE: 
#   A1: 106.094s                A1: 13.047s
#   A2: 67.859s                 A2: 11.062s
#   A3: 49.156s                 A3: 0.344s
#   A4:                         A4: 0.203s
#   A5:
#   A6:
#   A7: 0.922
#   A8: 0.203
#############################################################