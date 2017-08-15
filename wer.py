import io
import string
import os

def one_ref(fileName):
    one_ln = ''
    with io.open(fileName, 'r', encoding='utf-8') as f:
        for ln in f:
            for c in ['%HESITATION']:
                ln = ln.replace(c, " ")
            one_ln += ln.lower().rstrip('\n')
    return one_ln

def one_hyp(fileName):
    one_ln = ''
    with io.open(fileName, 'r', encoding='windows-1252') as f:
        for ln in f:
            for c in string.punctuation:
                ln = ln.replace(c, " ")
            one_ln += ln.lower().rstrip('\n')
    return one_ln


def gen_set(hyp_dir, ref_dir):
    out_hyp = io.open('one.hyp', 'w', encoding='utf-8')
    out_ref = io.open('one.ref', 'w', encoding='utf-8')
    for hyp in os.listdir(hyp_dir):
        if hyp.endswith('.txt'):
            print(hyp)

            ref = hyp.replace('txt', 'md')
            hyp_ln = one_hyp(hyp_dir + '/' + hyp)
            ref_ln = one_ref(ref_dir + '/SELTCAWRS_' + ref)
            out_hyp.write(hyp_ln + '\n')
            out_ref.write(ref_ln + '\n')
    out_hyp.close()
    out_ref.close()

# gen_set('trans', 'trans')
gen_set('trans/txt', 'trans/md')