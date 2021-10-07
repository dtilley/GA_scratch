""" Practice with *args and **kwargs 
 or changed to just parsing restart arguments."""
import pandas as pd


def main(args):
    if (len(args)==1):
        print('Evolutionary Algorithm (EA) running in normal model.')
        print('EA is of type (MU,LAMBDA) with an evolutionary strategy.')
        print('Number of Generation(s): '+str(args[0][1]))
        # Set EA parameters
        N_GEN = args[0][1]
        MU = 100
        LAMBDA = 2*MU
        outdir = args[0][0]
        print('Individuals/Generation: '+str(MU))
    else:
        argv = args[0]
        filenames = args[1]
        print('Evolutionary Algorithm (EA) running in restart model.')
        print('EA is of type (MU,LAMBDA) with an evolutionary strategy.')
        outdir = argv[0]
        pop_params = argv[1]
        pop_strategy = argv[2]
        pop_fitness = argv[3]
        hof_params = argv[4]
        hof_fitness = argv[5]
        new_hof = False
        previous_gens = argv[6]
        N_GEN = argv[7]
        if (N_GEN is None):
            N_GEN = 5
        print('Number of Generation(s): '+str(N_GEN))
        print('Number of Prior Generation(s): '+str(previous_gens))
        if (pop_params.shape[0] == pop_strategy.shape[0] == pop_fitness.shape[0]):
            MU = pop_params.shape[0]
            LAMBDA = 2*MU
            if (pop_params.shape[1] == pop_strategy.shape[1]):
                print('Individuals/Generation: '+str(MU))
            else:
                print('Population number of parameters did not match.')
                sys.exit()
        else:
            print('Check population size inputs did not match.')
            sys.exit()
        if (pop_params.shape[1] == hof_params.shape[1]):
            if (hof_params.shape[0] == hof_fitness.shape[0]):
                print('Hall of Fame contains: '+str(hof_params.shape[0])+' individuals.')
            else:
                print('Hall of Fame error.')
                new_hof = True
        print('Input Files:')
        for i in filenames:
            print('\t' + i)
        del filenames, args

if __name__ == '__main__':
    import os
    import sys
    if (len(sys.argv) == 1):
        print('Normal mode usage requires 2 positional arguments.')
        outstr = 'python '+sys.argv[0]+' outdir N_GENERATIONS'
        print(outstr)
        print('Restart mode usage requires 3 positional arguments.')
        outstr = 'python '+sys.argv[0]+' outdir indir N_GENERATIONS'
        print(outstr)
        sys.exit()
    elif (len(sys.argv) == 3):
        argv = [None]*2
        try:
            argv[1] = int(sys.argv[2])
        except ValueError:
            print('Number of generations to run must be integer.')
            sys.exit()
        if os.path.exists(sys.argv[1]):
            print('Output Directory: '+sys.argv[1])
            argv[0] = sys.argv[1]
            main((argv,))
        else:
            print('Cannot find directory: '+sys.argv[1])
            print('Default output directory: ./')
            argv[0] = './'
            main((argv,))
    elif (len(sys.argv) == 4):
        argv = [None]*8
        readfiles = [None]*6
        if os.path.exists(sys.argv[1]):
            print('Output Directory: '+sys.argv[1])
            argv[0] = sys.argv[1]
        else:
            print('Cannot find directory: '+sys.argv[1])
            print('Default output directory: ./')
            argv[0] = sys.argv[1]
        if os.path.exists(sys.argv[2]):
            print('Input Directory: '+sys.argv[2])
            path_in = sys.argv[2]
            filenames = os.listdir(path_in)
            readcnt = 0
            for i in filenames:
                if (i.find('pop_final_') >= 0):
                    filename = os.path.join(path_in, i)
                    argv[1] = pd.read_csv(filename, delimiter=' ')
                    readfiles[0] = i
                    readcnt += 1
                elif (i.find('pop_strategy_') >= 0):
                    filename = os.path.join(path_in, i)
                    argv[2] = pd.read_csv(filename, delimiter=' ')
                    readfiles[1] = i
                    readcnt += 1
                elif (i.find('pop_fitness_') >= 0):
                    filename = os.path.join(path_in, i)
                    argv[3] = pd.read_csv(filename, delimiter=' ')
                    readfiles[2] = i
                    readcnt += 1
                elif (i.find('hof_') >= 0 and i.find('_fitness_') <= 0):
                    filename = os.path.join(path_in, i)
                    argv[4] = pd.read_csv(filename, delimiter=' ')
                    readfiles[3] = i
                    readcnt += 1
                elif (i.find('hof_') >= 0 and i.find('_fitness_') >= 0):
                    filename = os.path.join(path_in, i)
                    argv[5] = pd.read_csv(filename, delimiter=' ')
                    readfiles[4] = i
                    readcnt += 1
                elif (i.find('logbook_') >= 0):
                    filename = os.path.join(path_in, i)
                    logfile = pd.read_csv(filename, delimiter=' ')
                    argv[6] = logfile.shape[0] - 1
                    readfiles[5] = i
                    readcnt += 1
            if (readcnt > 6):
                print('Read files exceeded maximum of 5.')
                sys.exit()
        else:
            print('Cannot find input directory: '+sys.argv[2])
            sys.exit()
        try:
            argv[7] = int(sys.argv[3])
        except ValueError:
            print('Number of generations to run must be integer.')
            sys.exit()
        main((argv, readfiles))
    else:
        print('Normal mode usage requires 2 positional arguments.')
        outstr = 'python '+sys.argv[0]+' outdir N_GENERATIONS'
        print(outstr)
        print('Restart mode usage requires 3 positional arguments.')
        outstr = 'python '+sys.argv[0]+' outdir indir N_GENERATIONS'
        print(outstr)
        sys.exit()
