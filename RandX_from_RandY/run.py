from RandRanger import RandRanger
from functools import partial

rr = RandRanger(500)

#print(rr.does_rand_even(4,8))
#print(rr.does_rand_reject(5,7))

#for runs in range(0,10):
#    print(rr.randX_from_randY_reject(5,7))

#for runs in range(0,10):
#    print(rr.randX_from_randY_reject(5,7, partial(rr.rand_always_n, 5) ))

bins = {0: '000', 1: '001', 2: '010', 3: '011', 4: '100', 5: '101', 6: '110', 7: '111'}

for num in bins:
    val = bins[num]
    print("{}: {} ({})".format(num, rr.to_bin_list(num), val))


for runs in range(0, 1):
    break
    results  = []
    
    #results.append(rr.run_trials(7, rr.best_x_from_y_function(5,7), 140))
    #results.append(rr.run_trials(7, rr.init_rand_distributed(140, 7), 140))
    results.append(rr.run_trials(7, rr.best_x_from_y_function(5,7, rr.init_rand_distributed(140, 5)), 140))
    #results.append(rr.run_trials(7, rr.best_x_from_y_function(5,10, rr.init_rand_distributed(140, 10)), 140))
    
    
    for res in results:
        func = res.func.__name__
        print("{}:\n {} ({})".format(func, res.spread, res.misses))
            
    
    #print("{}".format(rr.run_trials(7,7,rr.randX_from_randY_value, rr.init_rand_distributed(140), 140)))

    # break
    #
    # combo_gen = rr.build_combos(3, 6)
    # for foo in range(0,3):
    #     combo = next(combo_gen)
    #     print("{}".format(combo))
    #
    # print("(5) simple rand group:")
    # rr.spread_for_fn("rand5_r5", partial(rr.rand_n, 5), 5)
    #
    # print("\n(5) step group:")
    # rand_func = rr.rand_always_step
    # rr.spread_for_fn("step_r5", partial(rand_func, 5), 5)
    # rr.spread_for_fn("rem_r5_f7", partial(rr.rem_randX_from_randY, 5, 7, rand_func), 5)
    # rr.spread_for_fn("qual_r5_f7", partial(rr.qualify_randX_from_randY, 5, 7, rand_func), 5)
    # rr.spread_for_fn("bin_r5_f7", partial(rr.bin_randX_from_randY, 5, 7, rand_func), 5)
    #
    # print("\n(5) always exceed group:")
    # rand_func = rr.rand_always_exceed
    # rr.spread_for_fn("rem_r5_f7", partial(rr.rem_randX_from_randY, 5, 7, rand_func), 5)
    # rr.spread_for_fn("qual_r5_f7", partial(rr.qualify_randX_from_randY, 5, 7, rand_func), 5)
    #
    # print("\n(5) distr group:")
    # rand_func = rr.rand_distrib_steps
    # rr.spread_for_fn("step_r5", partial(rand_func, 5), 5)
    # rr.spread_for_fn("rem_r5_f7", partial(rr.rem_randX_from_randY, 5, 7, rand_func), 5)
    # rr.spread_for_fn("qual_r5_f7", partial(rr.qualify_randX_from_randY, 5, 7, rand_func), 5)
    # rr.spread_for_fn("bin_r5_f7", partial(rr.bin_randX_from_randY, 5, 7, rand_func), 5)
    #
    # ###
    #
    # print("\n(7) simple rand group:")
    # rand_func = rr.rand_n
    # rr.spread_for_fn("rand7_r7", partial(rand_func, 7), 7)
    # rr.spread_for_fn("bin_r7_f5", partial(rr.bin_randX_from_randY, 7, 5, rand_func), 7)
    #
    # print("\n(7) step group:")
    # rand_func = rr.rand_always_step
    # rr.spread_for_fn("step_r7", partial(rand_func, 7), 7)
    # rr.spread_for_fn("rem_r7_f5", partial(rr.rem_randX_from_randY, 7, 5, rand_func), 7)
    # rr.spread_for_fn("qual_r7_f5", partial(rr.qualify_randX_from_randY, 7, 5, rand_func), 7)
    # rr.spread_for_fn("bin_r7_f5", partial(rr.bin_randX_from_randY, 7, 5, rand_func), 7)
    #
    # print("\n(7) always exceed group:")
    # rand_func = rr.rand_always_exceed
    # rr.spread_for_fn("rem_r7_f5", partial(rr.rem_randX_from_randY, 7, 5, rand_func), 7)
    # rr.spread_for_fn("qual_r7_f5", partial(rr.qualify_randX_from_randY, 7, 5, rand_func), 7)
    #
    # print("\n(7) distr group:")
    # rand_func = rr.rand_distrib_steps
    # rr.spread_for_fn("step_r7", partial(rand_func, 7), 7)
    # rr.spread_for_fn("rem_r7_f5", partial(rr.rem_randX_from_randY, 7, 5, rand_func), 7)
    # rr.spread_for_fn("qual_r7_f5", partial(rr.qualify_randX_from_randY, 7, 5, rand_func), 7)
    # rr.spread_for_fn("bin_r7_f5", partial(rr.bin_randX_from_randY, 7, 5, rand_func), 7)
    #
    # print("\nlast group")
    #
    # #rr.spread_for_fn("rand_7_5", partial(rr.rem_randX_from_randY, 7, 5), 7)
    # #rr.spread_for_all("proof_rxy_5_7", 5, 7)
    #
    # #rr.spread_for_fn("rand7_5", partial(rr.randX_from_randY, 7, 5), 7)
    pass





