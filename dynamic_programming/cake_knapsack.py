def max_duffel_bag_value(cake_tuples, max_capacity):

    duffel_bag_value_dict = {}
    duffel_bag_value_dict[0] = 0

    cake_tuples_dict = {}

    for weight, value in cake_tuples:
        cake_tuples_dict[weight] = value

    for capacity in range(0,max_capacity+1):
        duffel_bag_value_dict[capacity] = 0

    max_value = 0

    for capacity in range(0,max_capacity+1):
        duffel_bag_sums = 0
        for first_addend in range(0,((capacity/2)+1)):
            second_addend = capacity - first_addend
            duffel_bag_sums = max(duffel_bag_sums, (duffel_bag_value_dict[first_addend]+ duffel_bag_value_dict[second_addend]))

        if capacity in cake_tuples_dict:
            max_value = max(duffel_bag_sums, cake_tuples_dict[capacity])
        else:
            max_value = duffel_bag_sums

        duffel_bag_value_dict[capacity] = max_value


    return max_value

# test values
cake_tuples = [(7,160), (3, 90), (2, 15)]
capacity    = 20



print (max_duffel_bag_value(cake_tuples, capacity))

