#!/usr/bin/python3

import xml.etree.ElementTree as _ET
from os.path import isfile as _isfile
from random import randint as _randint
from typing import Dict as _Dict, List as _List, Union as _Union
from xml.dom import minidom as _minidom

from .dict import index_by_value as _index_by_value
from ..encoding import UTF_8 as _UTF_8


def prettify(xml: _Union[_ET.Element, str], space: _Union[str, int] = '  ') -> str:
    """
    Prettifies a xml string or element

    Args:
        xml: XML string or `ElementTree.Element` to prettify
        space: The space before every new sub element

    Returns:
        The prettified string

    Examples:
        >>> print(prettify('<root><sub_elem></sub_elem></root>'))
        <root>
          <sub_elem/>
        </root>

    """
    if isinstance(space, int):
        space = ' ' * space

    if not isinstance(xml, str):
        reparsed = _minidom.parseString(_ET.tostring(xml, _UTF_8))
    else:
        reparsed = _minidom.parseString(bytes(xml, _UTF_8, errors='ignore'))

    pre_output = reparsed.toprettyxml(indent=space)
    return "\n".join(pre_output.split('\n')[1:])


class XMLManipulator:
    """Class to build a new xml element"""

    def __init__(self, fname_or_element: _Union[str, _ET.Element]):
        """
        Args:
            fname_or_element: File name of a xml file or a python xml `Element`
        """
        if isinstance(fname_or_element, str):
            if _isfile(fname_or_element):
                self.root = _ET.parse(fname_or_element).getroot()
            else:
                raise FileNotFoundError('The given file could not be found')
        else:
            self.root = fname_or_element

        self.root_id = 0
        self.elements = {0: self.root}

        for elem in self.root.iter():
            self.elements[_randint(111111111, 999999999)] = elem

    def add(self, parent_id: int, tag: str, text: str = '', **attrib) -> int:
        """
        Adds an element to a parent

        Args:
            parent_id: ID of the parent element
            tag: Tag / name of the new element
            text: Text of the new element
            **attrib: Attributes of the new element

        Returns:
            The id of the new created element

        """
        if parent_id == 0:
            element = _ET.Element(tag, **attrib)
            element.text = text
            self.root.append(element)
        elif parent_id in self.elements.keys():
            element = _ET.SubElement(self.elements[parent_id], tag, **attrib)
            element.text = text
        else:
            raise IndexError('The parent element does not exist')

        while True:  # do while would be nice
            elem_id = _randint(111111111, 999999999)
            if elem_id not in self.elements:
                break
        self.elements[elem_id] = element

        return elem_id

    def remove(self, id: int) -> None:
        """
        Removes a xml element

        Args:
            id: ID of the element

        """
        self.root.remove(self.elements[id])
        del self.elements[id]

    def update(self, id: int, new_tag: str = None, new_text: str = None, **new_attrib) -> None:
        """
        Updates a xml element

        Args:
            id: ID of the element
            new_tag: New tag of the element
            new_text: New text of the element
            new_attrib: New attributes of the element

        """
        elem = self.elements[id]
        if new_tag:
            elem.tag = new_tag
        if new_text:
            elem.text = new_text
        if new_attrib:
            elem.attrib = new_attrib

    def get_element(self, id: int) -> _ET.Element:
        """
        Returns the ids element

        Args:
            id: ID of the element

        Returns:
            The element

        """
        return self.elements[id]

    def get_id(self, tag: str, attrib: _Dict = None, parent_tag: str = None, parent_attrib: _Dict = {}) -> int:
        """
        Searches the element id by given attributes

        Args:
            tag: Tag of the element
            attrib: Attributes of the element
            parent_tag: Tag of the elements parent. May be useful if more than one element with the same name exists
            parent_attrib: Attributes of the elements parent. May be useful if more than one element with the same name exists

        Returns:
            The id of the element

        """
        if not parent_tag and not parent_attrib:
            for num, elem in self.elements.items():
                if tag == elem.tag:
                    if attrib:
                        if attrib == elem.attrib:
                            return num
                    else:
                        return num
        else:
            for elem in self.get_infos(tag, attrib, parent_tag, False):
                if elem['parent'].attrib == parent_attrib:
                    try:
                        return _index_by_value(self.elements, elem['element'])
                    except IndexError:
                        break

        raise ValueError('The element \'' + tag + '\' could not be found')

    def get_infos(self, tag: str, attrib: _Dict = None, parent_tag: str = None, stop_at_first=True) -> _Union[_Dict[str, _Union[_ET.Element, _List[_ET.Element], _List, None]],
                                                                                                              _List[_Dict[str, _Union[_ET.Element, _List[_ET.Element], _List, None]]]]:
        """
        Returns infos about a specific xml element

        Args:
            tag: Tag of the element from which you want to obtain the infos
            attrib: Attributes of the element. May be useful if more than one element with the same name exists
            parent_tag: Tag of the elements parent. May be useful if more than one element with the same name exists
            stop_at_first: If True only the first found element gets returned

        Returns:
            The xml element infos

        """
        elements = []

        if self.root.tag == tag and not parent_tag:
            if attrib and self.root.attrib == attrib:
                elements.append({'element': self.root, 'parent': None})
            else:
                elements.append({'element': self.root, 'parent': None})

        for element in self.root.iter():
            if elements and stop_at_first:
                return elements[0]

            if element.tag == tag:
                if parent_tag and parent_tag is not self.root.tag:
                    continue

                if attrib and element.attrib == attrib:
                    elements.append({'element': element, 'parent': self.root})
                else:
                    elements.append({'element': element, 'parent': self.root})

            for sub_element in element:
                if elements and stop_at_first:
                    return elements[0]

                if sub_element.tag == tag:
                    if parent_tag and parent_tag is not element.tag:
                        continue

                    if attrib and sub_element.attrib == attrib:
                        elements.append({'element': sub_element, 'parent': element})
                    else:
                        elements.append({'element': sub_element, 'parent': element})

        return elements

    def get_string(self, pretty_print=True) -> str:
        """
        Returns the xml as a string

        Notes:
            If you want to get the XML element, use `XMLBuilder.root`

        Args:
            pretty_print: If True the string to be return will be prettified

        Returns:
            The built xml as string

        """
        if pretty_print:
            return prettify(self.root)
        else:
            return _ET.tostring(self.root, _UTF_8)


def new_xml(root_element='root') -> XMLManipulator:
    """
    Creates a new xml element

    Args:
        root_element: Name of the xml root element

    Returns:
        The xml manipulator to edit the new xml

    """
    return XMLManipulator(_ET.Element(root_element))
