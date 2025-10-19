from enum import Enum

class BlockType(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"


def block_to_block_type(block):
    if block.startswith("#"):
        return BlockType.HEADING
    if block.startswith("```") and block.endswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        return BlockType.QUOTE
    if block.startswith("- "):
        return BlockType.UNORDERED_LIST
    if block[0].isdigit():
        blockSplit = block.split("\n")
        counter = 1
        is_ordered = True
        for i in blockSplit:
            if not i[0].isdigit() and i[1:3] != ". " and i[0] == str(counter):
                is_ordered = False
                break
            counter += 1
        if is_ordered:
            return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH
        