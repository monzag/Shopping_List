# Shopping List

## Classes

### Item
A thing to buy.

#### Attributes:
* `name`
* `quantity` (wielkość)
* `unit` - quantity unit (ilość wyrażona w danej jednostce)
* `price_per_unit`
* `categories` - list of categories that this item belongs to e.g: ["food", "vegetables"]
* `is_bought` - is the item already bought

#### Methods:

##### `__init__`

Parameters:
* `name`
* `quantity`
* `unit`
* `price_per_unit`
* `categories`
* `is_bought`

##### `__str__()`
Return Item in proper format {name} {is_bought}

##### `__eq__()`
Compare two objects

##### `get_total_price()` 
price * quantity

### ShoppingList
Used to aggregate shopping items

#### Attributes:
* `name`
* `date`
* `items`

#### Methods:

##### `__init__`

Parameters:
* `name`
* `date`
* `items`

##### `get_items(is_bought)`
Returns list of bought or not bought items

##### `get_total_price()` 
Return total price of the shopping list

##### `sort_by(attr)` 
Sort items by quantity/price/name

##### `create_from_csv`
Get data from csv file

##### `save_to_csv`
Save data to csv file

##### `show_all_list`
Display list with all items

## Main
Run application

## Controller
Manages methods of objects and view

## View
All inputs, prints and look

## shopping.csv
File with data

