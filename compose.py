import os
from tqdm import tqdm
from shutil import copyfile

def compose(dataset):
    with open('./labels/' + dataset + ".txt") as fh:
        sets = (fh.read().split('\n'))
        dt = {}
        for row in sets:
            try:
                kv = row.split(' ')
                key = kv[0]
                val = kv[1]
                dt[key] = (val)
            except:
                print("Invalid entry : {0}, skipping this row..".format(row))
        return dt

test = compose('test')
train = compose('train')
val = compose('val')

# merge everything into a single dictionary
mg = {**test, **train, **val}

merged = {}
for item in mg:
    if not mg[item] in merged:
        merged[mg[item]] = []

    merged[(mg[item])].append(item)


classes = [
    'letter',
    'form',
    'email',
    'handwritten',
    'advertisement',
    'scientific report',
    'scientific publication',
    'specification',
    'file folder',
    'news article',
    'budget',
    'invoice',
    'presentation',
    'questionnaire',
    'resume',
    'memo'
]

for category in tqdm(merged, "Total progress"):
    # save directory is here

    real_cat = classes[int(category)]

    target = './dataset' + '/' + real_cat + "/"

    for item in tqdm(merged[category], "Building files for next category.."):
        path = item
        base_name = os.path.basename(path)

        if not os.path.isdir(target):
            os.makedirs(target)

        copyfile('./images/' + path, target + base_name)