import utils
import sorts

def title_ascending(book1,book2):
    return book1["title_lower"]> book2["title_lower"]

def author_ascending(book1,book2):
    return book1["author_lower"]> book2["author_lower"]

def by_total_length(book1,book2):
    return (len(book1["author_lower"]) +len(book1["title_lower"]))> (len(book2["author_lower"])+len(book2["title_lower"]))


bookshelf = utils.load_books('books_small.csv')
bookshelf_v1 = bookshelf.copy()
bookshelf_v2 = bookshelf.copy()
long_bookshelf = utils.load_books('books_large.csv')
long_bookshelf_v2 = long_bookshelf.copy()


sort1 = sorts.bubble_sort(bookshelf,title_ascending)


sort2 = sorts.bubble_sort(bookshelf_v1,author_ascending)
sort3 = sorts.quicksort(bookshelf_v2,0,len(bookshelf)-1,author_ascending)

for i in bookshelf_v2:
    print(i["author"])

sort4 = sorts.bubble_sort(long_bookshelf,by_total_length)
# for i in long_bookshelf:
#     print(len(i["title"]) + len(i["author"]))

sort5 = sorts.quicksort(long_bookshelf_v2,0,len(long_bookshelf_v2)-1,by_total_length)
# for i in sort5:
#     print(len(i["title"]) + len(i["author"]))
