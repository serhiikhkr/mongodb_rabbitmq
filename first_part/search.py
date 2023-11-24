from models import Author, Quote
import connect


def search_quotes(comm):
    parts = comm.split(':')
    if len(parts) != 2:
        print("Invalid command format.")
        return
    parts[1] = parts[1].strip()
    search_type, search_value = parts
    if search_type == 'name':
        author = Author.objects(fullname=search_value).first()
        if author:
            quotes = Quote.objects(author=author)
            for q in quotes:
                print(q.quote)
        else:
            print(f"No quotes found for author '{search_value}'.")
    elif search_type == 'tag':
        quotes = Quote.objects(tags__in=[search_value])
        for q in quotes:
            print(q.quote)
    elif search_type == 'tags':
        tags = search_value.split(',')
        quotes = Quote.objects(tags__in=tags)
        for q in quotes:
            print(q.quote)
    else:
        print("Invalid search type.")


if __name__ == '__main__':
    while True:
        command = input("Enter command (name: author_name, tag: tag_name, tags: tag1,tag2, ..., exit to quit): ")
        if command.lower() == 'exit':
            break
        search_quotes(command)
