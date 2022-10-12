import csv
import copy


def distributor() -> list[dict[str, None]]:
    """
    Функция считывания csv файла
    :return: Возвращает отсортированный файл в виде списка словарей
    """
    results = []
    with open('ads.csv', encoding='utf-8') as File:
        reader = csv.DictReader(File)
        for row in reader:
            results.append(row)
        return results


res = distributor()
res2 = copy.deepcopy(res)

authors = set([i['author'] for i in res])
authors_list = []
for i, v in enumerate(authors):
    authors_list.append(dict({'author_id': i + 1, 'author': v}))



address = list(set([i['address'] for i in res]))
address_list = []
for i, v in enumerate(address):
    address_list.append(dict({'address': v, 'address_id': i + 1}))
print(address)
print(address_list)


for i in range(len(res2)):
    for j in authors_list:
        if res2[i]['author'] == j['author']:
            res2[i]['author'] = j['author_id']

for i in range(len(res2)):
    for j in address_list:
        print(j['address'])
        print(res2[i]['address'])
        if res2[i]['address'] == j['address']:
            res2[i]['address'] = j['address_id']


def write_author(x):
    fieldnames = ['author_id', 'author']
    with open('author.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(x)


def write_address(x):
    fieldnames = ['address_id', 'address']
    with open('address.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(x)


def write_add(x):
    fieldnames = ['Id', 'name', 'author', 'price', 'description', 'address', 'is_published']
    with open('ads.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(x)


def main():
    write_author(authors_list)
    write_address(address_list)
    write_add(res2)


if __name__ == '__main__':
    main()
