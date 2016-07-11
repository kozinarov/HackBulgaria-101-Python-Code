import sys
import collections


class Polynomials:
    def __init__(self, multipliers, degrees):
        self._multipliers = multipliers
        self._degrees = degrees

    def get_multipliers(self):
        return self._multipliers

    def get_degrees(self):
        return self._degrees

    def find_equal(self):
        return [item for item, count in collections.Counter(self._degrees).items() if count > 1]

    def find_equal_by_positins(self):
        equal = self.find_equal()
        equal_dic = {}
        cnt = 0
        for item in equal:
            for i in range(0, len(self._degrees)):
                if item == self._degrees[i]:
                    if item in equal_dic:
                        equal_dic[item].append(i)
                    else:
                        equal_dic.setdefault(item, []).append(i)
                    if(cnt > 0):
                        del(self._degrees[i])
                    cnt += 1
            cnt = 0

        return equal_dic

    def sum_equal(self):
        equal_dic = self.find_equal_by_positins()
        tmp_mult = []
        for items in equal_dic:
            # ne znam dali mi trqbva za sega tmp_deg = items
            cnt = 0
            for elem_like_index in equal_dic[items]:
                tmp_mult.append(self._multipliers[elem_like_index])
                if cnt == 0:
                    tmp_ind = elem_like_index
                if cnt > 0:
                    del(self._multipliers[elem_like_index])
                cnt += 1
            self._multipliers[tmp_ind] = sum(tmp_mult)
            cnt = 0
            tmp_mult = 0
        print('The derivative of f(x) = {} is:'.format(self.convert_to_polynom(0)))

    def derivative(self):
        # moje i len(self._degrees) zashtoto tqxnata duljina e ednakva
        for i in range(0, len(self._multipliers)):
            self._multipliers[i] = self._multipliers[i] * self._degrees[i]
            self._degrees[i] = self._degrees[i] - 1

    def convert_to_polynom(self, swich):
        polynom = ""
        if swich == 1:
            tmp = self._multipliers
        elif swich == 0:
            tmp = self._degrees

        for i in range(0, len(tmp)):
            # if self._multipliers[i] == 1:
            #     pass
            # else:
            polynom += str(self._multipliers[i])

            if self._degrees[i] == 0:
                pass
            elif self._degrees[i] == 1:
                polynom += 'x'
            else:
                polynom += 'x^'
                polynom += str(self._degrees[i])

            if i != len(tmp) - 1:
                polynom += ' + '

        return polynom


def main():
    polinom = sys.argv[1]
    multipliers = []
    degrees = []
    tmp = []
    polinom = polinom.split(' + ')
    for elem in polinom:
        if elem.endswith('x'):
            tmp.append(elem.split('x'))
        else:
            tmp.append(elem.split('x^'))
    for elem in tmp:
        if elem[0] != '':
            multipliers.append(int(elem[0]))
        else:
            multipliers.append(1)

        if elem[1] != '':
            degrees.append(int(elem[1]))
        else:
            degrees.append(1)

    a = Polynomials(multipliers, degrees)
    a.sum_equal()
    a.derivative()
    print("f'(x) = {}".format(a.convert_to_polynom(1)))


if __name__ == '__main__':
    main()
