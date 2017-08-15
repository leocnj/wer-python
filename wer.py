import io
import string
import os
import re

def one_ref(fileName, id):
    one_ln = id
    with io.open(fileName, 'r', encoding='windows-1252') as f:
        for ln in f:
           ln = ln.lower().rstrip('\n')
           if re.search(r't\d+_v\d+', ln):
                pass
           else:
               for c in string.punctuation:
                   ln = ln.replace(c, " ")
               one_ln += " " + ln
    return one_ln


def one_hyp(fileName, id):
    one_ln = id + ' '
    with io.open(fileName, 'r', encoding='utf-8') as f:
        for ln in f:
            for c in ['%HESITATION', '*']:
                ln = ln.replace(c, " ")
            one_ln += ln.lower().rstrip('\n')
    return one_ln


def gen_set(ref_dir, hyp_dir):
    out_hyp = io.open('one.hyp', 'w', encoding='utf-8')
    out_ref = io.open('one.ref', 'w', encoding='utf-8')

    for ref in os.listdir(ref_dir):
        if ref.endswith('.txt'):
            print(ref)
            id = os.path.basename(ref)

            hyp = ref.replace('txt', 'md')
            ref_ln = one_ref(ref_dir + '/' + ref, id)
            hyp_ln = one_hyp(hyp_dir + '/SELTCAWRS_' + hyp, id)
            out_hyp.write(hyp_ln + '\n')
            out_ref.write(ref_ln + '\n')
    out_hyp.close()
    out_ref.close()

# gen_set('trans', 'trans')
gen_set('trans/txt', 'trans/md')