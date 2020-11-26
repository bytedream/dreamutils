# dreamutils

<p align="center"><h5>A collection of useful and often repeated python methods</h5></p>

---

The package contains code / method that were written over and over again,
without creating a centralized package for them. It project was created to solve this problem.
Surely, some of the methods are exotic(most of the `dreamutils.python` file i think),
but if you need those methods you know where to find them.


<p align="center">
    <a href="#Installation">Installation</a>
    •
    <a href="#Examples">Examples</a>
    •
    <a href="#Licence">Licence</a>
</p>


## Installation
- Use `Python >= 3.6`

- Install it
    - via `pip`
    ```bash
    pip install dreamutils
    ```
    - or with `git`
    ```bash
    git clone https://github.com/ByteDream/dreamutils.git
    cd dreamutils
    python setup.py install
    ```

## Examples

Here are examples of some useful packages

#### XML

A easy to use and powerful xml manipulation class
```python
import dreamutils.types.xml as xml

my_xml = xml.new_xml()
sub_elem_id = my_xml.add(0, 'sub_elem', 'example_text')
# every new created element has an id

my_xml.get_element(sub_elem_id).attrib = {'attrib': 'example'}
# with the id you can obtain the element later...
my_xml.add(sub_elem_id, 'sub_sub_elem')
# ... and use it to add new sub element

# Note: the root element has always the id `0`

print(my_xml.get_string())
```

#### Sorting

A collection of sorting algorithms (the most common I think)

```python
from dreamutils.sort import QuickSort

sorted = QuickSort.integer([2, 9, 4, 623, 5])
print(sorted)
```

#### Net

A file with nice internet methods

```python
from dreamutils.net import get_ip_infos

infos = get_ip_infos('8.8.8.8')
# if no argument is passed, information about your own ip will be returned
print(infos)
```

## Testing

**The tools are (currently) only tested on linux, but they should also work on Windows and MacOS.**

So if there are any problems feel free to open a new [issue](https://github.com/ByteDream/dreamutils/issues/new).


## Licence 

This project is licensed under the GNU Lesser General Public License v3.0 (LGPL-3.0) - see the [LICENSE](LICENCE) file for more details.