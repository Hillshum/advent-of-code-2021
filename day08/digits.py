from dataclasses import dataclass
from typing import List

input_string = """be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce"""


with open('input.txt', 'r') as f:
    input_string = f.read()

UNIQUES = set([2, 3, 4, 7])
display_strings = input_string.strip().split('\n')

@dataclass
class Display:
    inputs: List[str]
    outputs: List[str]

    @classmethod
    def from_string(cls, s):
        ins, outs = s.split('|')
        return Display(ins.strip().split(' '), outs.strip().split(' '))


displays = [*map(Display.from_string, display_strings)]

outputs = [ digit for display in displays for digit in display.outputs  ]


target = 0
for i in outputs:
    if len(i) in UNIQUES:
        target += 1

print(target)
# output_lens = map(len)

# print(displays)
