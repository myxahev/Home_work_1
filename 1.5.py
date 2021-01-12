gain, costs = int(input('input gain: ')), int(input('input costs: '))
proceeds = gain + costs
if proceeds > costs:
    print('The company operates in profit')
    profitability = gain / proceeds * 100
    print(f'profitability your company: {profitability}%')
    staff_members = int(input('input number of staff'))
    revenue_per_employee = proceeds / staff_members
    print(f'Revenue per employee = {revenue_per_employee}')
else:
    print('The company operates at a loss')