
import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
import pandas as pd

data = pd.read_csv(
    "/home/gabriel/Descargas/survey_results_public.csv", low_memory=False)

# aa = data[['Age', 'IDE']]
aa = data[['Age', 'LanguageWorkedWith']]
bb = aa.dropna()

age = bb['Age']
ages = []
for a in age:
    if a.startswith('Under'):
        ages.append(18)
    elif a.endswith('older'):
        ages.append(65)
    else:
        ages.append((float(a[:2]) + float(a[5:7])) / 2.)
ages = np.array(ages)
ages_vals = (18.0, 21.0, 29.5, 39.5, 49.5, 59.5, 65.0)

# # ydata = bb['IDE']
# # data_vals = []
# # for i in ydata:
# #     data_vals += i.split(';')
# # print(set(data_vals))
# data_dict = {
#     'Sublime Text': [0, 0, 0, 0, 0, 0, 0], 'Notepad++': [0, 0, 0, 0, 0, 0, 0],
#     'TextMate': [0, 0, 0, 0, 0, 0, 0], 'Eclipse': [0, 0, 0, 0, 0, 0, 0],
#     'Coda': [0, 0, 0, 0, 0, 0, 0], 'Vim': [0, 0, 0, 0, 0, 0, 0],
#     'Atom': [0, 0, 0, 0, 0, 0, 0], 'Android Studio': [0, 0, 0, 0, 0, 0, 0],
#     'Emacs': [0, 0, 0, 0, 0, 0, 0], 'Xcode': [0, 0, 0, 0, 0, 0, 0],
#     'IPython / Jupyter': [0, 0, 0, 0, 0, 0, 0],
#     'RStudio': [0, 0, 0, 0, 0, 0, 0], 'Zend': [0, 0, 0, 0, 0, 0, 0],
#     'PHPStorm': [0, 0, 0, 0, 0, 0, 0], 'IntelliJ': [0, 0, 0, 0, 0, 0, 0],
#     'RubyMine': [0, 0, 0, 0, 0, 0, 0], 'NetBeans': [0, 0, 0, 0, 0, 0, 0],
#     'PyCharm': [0, 0, 0, 0, 0, 0, 0], 'Komodo': [0, 0, 0, 0, 0, 0, 0],
#     'Visual Studio Code': [0, 0, 0, 0, 0, 0, 0],
#     'Visual Studio': [0, 0, 0, 0, 0, 0, 0],
#     'Light Table': [0, 0, 0, 0, 0, 0, 0]
# }

# ydata = bb['LanguageWorkedWith']
# data_vals = []
# for i in ydata:
#     data_vals += i.split(';')
# print(set(data_vals))
data_dict = {
    'HTML': [0, 0, 0, 0, 0, 0, 0], 'C++': [0, 0, 0, 0, 0, 0, 0],
    'Lua': [0, 0, 0, 0, 0, 0, 0], 'Assembly': [0, 0, 0, 0, 0, 0, 0],
    'Groovy': [0, 0, 0, 0, 0, 0, 0], 'JavaScript': [0, 0, 0, 0, 0, 0, 0],
    'Objective-C': [0, 0, 0, 0, 0, 0, 0], 'Cobol': [0, 0, 0, 0, 0, 0, 0],
    'Hack': [0, 0, 0, 0, 0, 0, 0], 'Clojure': [0, 0, 0, 0, 0, 0, 0],
    'CSS': [0, 0, 0, 0, 0, 0, 0], 'Go': [0, 0, 0, 0, 0, 0, 0],
    'C': [0, 0, 0, 0, 0, 0, 0], 'Erlang': [0, 0, 0, 0, 0, 0, 0],
    'R': [0, 0, 0, 0, 0, 0, 0], 'CoffeeScript': [0, 0, 0, 0, 0, 0, 0],
    'Scala': [0, 0, 0, 0, 0, 0, 0], 'Perl': [0, 0, 0, 0, 0, 0, 0],
    'Java': [0, 0, 0, 0, 0, 0, 0], 'PHP': [0, 0, 0, 0, 0, 0, 0],
    'Visual Basic 6': [0, 0, 0, 0, 0, 0, 0], 'C#': [0, 0, 0, 0, 0, 0, 0],
    'SQL': [0, 0, 0, 0, 0, 0, 0], 'TypeScript': [0, 0, 0, 0, 0, 0, 0],
    'VBA': [0, 0, 0, 0, 0, 0, 0], 'Python': [0, 0, 0, 0, 0, 0, 0],
    'Matlab': [0, 0, 0, 0, 0, 0, 0], 'Julia': [0, 0, 0, 0, 0, 0, 0],
    'Swift': [0, 0, 0, 0, 0, 0, 0], 'Rust': [0, 0, 0, 0, 0, 0, 0],
    'Haskell': [0, 0, 0, 0, 0, 0, 0], 'F#': [0, 0, 0, 0, 0, 0, 0],
    'Delphi/Object Pascal': [0, 0, 0, 0, 0, 0, 0],
    'Bash/Shell': [0, 0, 0, 0, 0, 0, 0], 'Ocaml': [0, 0, 0, 0, 0, 0, 0],
    'Ruby': [0, 0, 0, 0, 0, 0, 0], 'VB.NET': [0, 0, 0, 0, 0, 0, 0],
    'Kotlin': [0, 0, 0, 0, 0, 0, 0]}

idx = 0
for _, row in bb.iterrows():
    for y in row['LanguageWorkedWith'].split(';'):  # IDE
        data_dict[y][ages_vals.index(ages[idx])] += 1
    idx += 1

ages_sum = np.zeros(7)
for key, vals in data_dict.items():
    ages_sum += np.array(vals)

for key, vals in data_dict.items():
    data_dict[key] = np.array(vals) / ages_sum

# ages_vals = (18.0, 21.0, 29.5, 39.5, 49.5, 59.5, 65.0)
# data_dict = {'Sublime Text': np.array([0.08369769, 0.10623334, 0.10345275, 0.07639966, 0.05874223,
#        0.04820333, 0.03547672]), 'Notepad++': np.array([0.11825942, 0.10461349, 0.11594328, 0.11874545, 0.13003916,
#        0.12971078, 0.09090909]), 'TextMate': np.array([0.00229024, 0.00178388, 0.00308475, 0.00651961, 0.00714121,
#        0.00657318, 0.01773836]), 'Eclipse': np.array([0.06579221, 0.06151323, 0.05739799, 0.0622211 , 0.07809261,
#        0.0907099 , 0.0864745 ]), 'Coda': np.array([0.00312305, 0.00202994, 0.00167767, 0.00262683, 0.00310988,
#        0.00438212, 0.01773836]), 'Vim': np.array([0.06037893, 0.07711708, 0.09331096, 0.10627591, 0.1015895 ,
#        0.09859772, 0.05986696]), 'Atom': np.array([0.08702894, 0.07047365, 0.0589566 , 0.05310631, 0.04353836,
#        0.03768624, 0.04656319]), 'Android Studio': np.array([0.08952738, 0.07855239, 0.06026626, 0.04516252, 0.04181064,
#        0.043383  , 0.04878049]), 'Emacs': np.array([0.01165938, 0.00953455, 0.01221994, 0.02133114, 0.03086846,
#        0.04469763, 0.04878049]), 'Xcode': np.array([0.03601915, 0.03007997, 0.03624851, 0.0344653 , 0.04872149,
#        0.04907975, 0.06651885]), 'IPython / Jupyter': np.array([0.02144493, 0.02628665, 0.02577119, 0.02417951, 0.02326653,
#        0.02453988, 0.02217295]), 'RStudio': np.array([0.00374766, 0.00984212, 0.01124581, 0.01272273, 0.01462797,
#        0.02015776, 0.02217295]), 'Zend': np.array([0.00124922, 0.00090219, 0.00103907, 0.00126594, 0.00161253,
#        0.00306748, 0.01330377]), 'PHPStorm': np.array([0.01998751, 0.0321099 , 0.03169174, 0.02544545, 0.01647086,
#        0.01533742, 0.01995565]), 'IntelliJ': np.array([0.08036644, 0.08864056, 0.0860158 , 0.08181156, 0.06231283,
#        0.05828221, 0.05321508]), 'RubyMine': np.array([0.00458047, 0.00416239, 0.00583396, 0.00515872, 0.00575904,
#        0.00613497, 0.01552106]), 'NetBeans': np.array([0.03018946, 0.03280705, 0.0225782 , 0.0200652 , 0.02614605,
#        0.02979842, 0.0443459 ]), 'PyCharm': np.array([0.05121799, 0.04748821, 0.0398528 , 0.03351584, 0.02925593,
#        0.028922  , 0.0421286 ]), 'Komodo': np.array([0.00312305, 0.0013738 , 0.00129884, 0.00269013, 0.0029947 ,
#        0.00569676, 0.02217295]), 'Visual Studio Code': np.array([0.10306059, 0.11232315, 0.12258902, 0.12545495, 0.11091914,
#        0.08194566, 0.06651885]), 'Visual Studio': np.array([0.12200708, 0.10155834, 0.10913519, 0.14004494, 0.16217461,
#        0.17134093, 0.14634146]), 'Light Table': np.array([0.00124922, 0.00057412, 0.00038965, 0.00079121, 0.00080627,
#        0.00175285, 0.01330377])}

fig = plt.figure(figsize=(10, 10))
# plt.style.use('seaborn-darkgrid')
# plot_ydata = (
#     'Sublime Text', 'Vim', 'Notepad++', 'IPython / Jupyter', 'Atom', 'PyCharm',
#     'RStudio', 'Visual Studio Code', 'Visual Studio', 'Emacs', 'IntelliJ',
#     'Eclipse', 'Light Table', 'Komodo')
plot_ydata = ('Java', 'JavaScript', 'Python', 'C#', 'C')

lines = ["-", "--", "-.", ":"]
linecycler = cycle(lines)
posxcycler = cycle((ages_vals[-1] + 1., ages_vals[0] - 1.))
posycycler = cycle((-1, 0))
algncycler = cycle(('left', 'right'))

for key in plot_ydata:
    vals = data_dict[key]
    p = plt.plot(
        ages_vals, 100. * np.array(vals), label=key, ls=next(linecycler))
    plt.annotate(
        key, (next(posxcycler), 100. * vals[next(posycycler)]),
        horizontalalignment=next(algncycler), color=p[0].get_color())
plt.xticks(
    ages_vals, ('<18', '18-24', '25-34', '35-44', '45-54', '55-64', '>65'))
# plt.legend(loc='upper center', bbox_to_anchor=(0.47, 1.17), ncol=3)
plt.xlabel("Age ranges", fontsize=14)
plt.ylabel("Usage %", fontsize=14)
plt.xlim(7, 70)

plt.title("Stack Overflow Developer Survey 2018")
plt.box(False)
plt.grid()
fig.tight_layout()
plt.savefig('/home/gabriel/Descargas/SO_2018.png', dpi=300)
