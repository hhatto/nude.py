#!/usr/bin/env python
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import imp
import os
import multiprocessing

name = 'nude'
fp, pathname, description = imp.find_module(name, ['..'])

try:
    nude = imp.load_module(name, fp, pathname, description)
except Exception as e:
    print(e)
finally:
    if fp:
        fp.close()


def testfile(fname, resize=False):
    n = nude.Nude(fname)
    if resize:
        n.resize(maxheight=800, maxwidth=600)
    n.parse()
    return n.result


def nudecallback(result):
    global results
    if result:
        results['tp'] += 1
    else:
        results['fn'] += 1


def notnudecallback(result):
    global results
    if result:
        results['fp'] += 1
    else:
        results['tn'] += 1


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        description='Tests the true positive and false positive rate.')
    parser.add_argument('-r', '--resize', action='store_true',
                        help='Reduce image size to increase speed of scanning')
    parser.add_argument('-t', '--threads', metavar='int', type=int,
                        required=False, default=0, help='The number of threads to start')
    args = parser.parse_args()

    if args.threads < 1:
        args.threads = None

    pool = multiprocessing.Pool(args.threads)
    results = {}
    results['tp'] = 0
    results['tn'] = 0
    results['fp'] = 0
    results['fn'] = 0
    nudepath = os.path.join('samples', 'nude')
    notnudepath = os.path.join('samples', 'not_nude')
    for nudepic in os.listdir(nudepath):
        fname = os.path.join(nudepath, nudepic)
        pool.apply_async(testfile, (fname, ), {
                         'resize': args.resize}, nudecallback)

    for notnudepic in os.listdir(notnudepath):
        fname = os.path.join(notnudepath, notnudepic)
        pool.apply_async(testfile, (fname, ), {
                         'resize': args.resize}, notnudecallback)

    pool.close()
    pool.join()
    nudenum = results['tp'] + results['fn']
    nonnudenum = results['fp'] + results['tn']
    if nudenum:
        print("True positives: ", results[
              'tp'], '/', nudenum, ' - ', (results['tp'] / nudenum) * 100, '%', sep='')
    else:
        print("True positives: N/A")
    if nonnudenum:
        print("False positives: ", results[
              'fp'], '/', nonnudenum, ' - ', (results['fp'] / nonnudenum) * 100, '%', sep='')
    else:
        print("False positives: N/A")
