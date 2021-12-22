from dataclasses import dataclass
from collections import defaultdict
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

LENGHTS = {
    2: [1],
    3: [7],
    4: [4],
    5: [2,3,5],
    6: [0,6,9],
    7: [8]
    
}

@dataclass
class Display:
    inputs: List[str]
    outputs: List[str]

    @classmethod
    def from_string(cls, s):
        ins, outs = s.split('|')
        return Display(ins.strip().split(' '), outs.strip().split(' '))

    def parse(self):
        by_length = defaultdict(list) 
        for i in self.inputs:
            by_length[len(i)].append(i) 
        print(by_length)

        mappings = {}

        mappings[7] = set(by_length[3][0])
        mappings[1] = set(by_length[2][0])
        # mappings['a'] = seven - one

        mappings[6] = set(next(filter(lambda x:  not (set(x) > mappings[1]), by_length[6])))
        by_length[6] = [x for x in by_length[6] if set(x) != mappings[6] ]
        # print(by_length, six)
        # mappings['c'] = one - six

        mappings[4] = set(by_length[4][0])
        # print(four)

        mappings[9] = set(next(filter(lambda x: set(x) > mappings[4], by_length[6])))
        by_length[6] = [x for x in by_length[6] if set(x) != mappings[9] ]

        mappings[8] = set(by_length[7][0])

        mappings[0] = set(by_length[6][0])

        # mappings['e'] = eight - nine
        # print(nine)

        # mappings['d'] = eight - zero

        mappings[3] = set(next(filter(lambda x: set(x) > mappings[1], by_length[5])))
        by_length[5] = [x for x in by_length[5] if set(x) != mappings[3] ]

        # mappings['g'] = three - four - seven


        mappings[5] = set(next(filter(lambda x: set(x) < mappings[6], by_length[5])))
        by_length[5] = [x for x in by_length[5] if set(x) != mappings[5] ]

        # mappings['e'] = six - five


        mappings[2] = set(by_length[5][0])





        # print(mappings)
        return {frozenset(v): k for k,v in mappings.items()}

    def decode_output(self):
        mappings = self.parse()
        return int("".join([str(mappings[frozenset(i)]) for i in self.outputs]))


displays = [*map(Display.from_string, display_strings)]

outputs = [ digit for display in displays for digit in display.outputs  ]


target = 0
for i in outputs:
    if len(i) in UNIQUES:
        target += 1

print(target)
# output_lens = map(len)

# print(displays)
test_display = Display.from_string('acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf')
print(test_display.decode_output())

decoded_output = sum([d.decode_output() for d in displays])

print(decoded_output)