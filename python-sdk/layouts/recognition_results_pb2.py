# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recognition_results.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19recognition_results.proto\x12\x04main\"\xce\x02\n\x08\x44ocument\x12\x0f\n\x07version\x18\x01 \x01(\x05\x12#\n\ncharacters\x18\x02 \x03(\x0b\x32\x0f.main.Character\x12\x19\n\x05pages\x18\x03 \x03(\x0b\x32\n.main.Page\x12\x1b\n\x06tables\x18\x04 \x03(\x0b\x32\x0b.main.Table\x12$\n\x0btable_cells\x18\x05 \x03(\x0b\x32\x0f.main.TableCell\x12\x19\n\x05\x66onts\x18\x06 \x03(\x0b\x32\n.main.Font\x12\"\n\nfont_sizes\x18\x07 \x03(\x0b\x32\x0e.main.FontSize\x12$\n\x0b\x66ont_styles\x18\x08 \x03(\x0b\x32\x0f.main.FontStyle\x12\x1d\n\x07headers\x18\t \x03(\x0b\x32\x0c.main.Header\x12\x1d\n\x07\x66ooters\x18\n \x03(\x0b\x32\x0c.main.Footer\x12\x0b\n\x03md5\x18\x12 \x01(\x0c\"T\n\tCharacter\x12\x0f\n\x07unicode\x18\x01 \x01(\r\x12\r\n\x05\x65rror\x18\x02 \x01(\r\x12\'\n\x0c\x62ounding_box\x18\x03 \x01(\x0b\x32\x11.main.BoundingBox\"h\n\x04Page\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.main.CharacterRange\x12\r\n\x05width\x18\x02 \x01(\r\x12\x0e\n\x06height\x18\x03 \x01(\r\x12\r\n\x05\x64pi_x\x18\x04 \x01(\r\x12\r\n\x05\x64pi_y\x18\x05 \x01(\r\"(\n\x05Table\x12\n\n\x02id\x18\x01 \x01(\r\x12\x13\n\x0bpage_number\x18\x02 \x01(\r\"\xd5\x01\n\tTableCell\x12\n\n\x02id\x18\x01 \x01(\r\x12\'\n\x0c\x62ounding_box\x18\x02 \x01(\x0b\x32\x11.main.BoundingBox\x12%\n\x10\x62\x61\x63kground_color\x18\x03 \x01(\x0b\x32\x0b.main.Color\x12\x19\n\x11left_border_width\x18\x04 \x01(\r\x12\x1a\n\x12right_border_width\x18\x05 \x01(\r\x12\x18\n\x10top_border_width\x18\x06 \x01(\r\x12\x1b\n\x13\x62ottom_border_width\x18\x07 \x01(\r\"[\n\x04\x46ont\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.main.CharacterRange\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\r\n\x05serif\x18\x03 \x01(\x08\x12\x11\n\tmonospace\x18\x04 \x01(\x08\"=\n\x08\x46ontSize\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.main.CharacterRange\x12\x0c\n\x04size\x18\x02 \x01(\r\"u\n\tFontStyle\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.main.CharacterRange\x12$\n\x05style\x18\x02 \x01(\x0e\x32\x15.main.FontStyle.Style\"\x1d\n\x05Style\x12\x08\n\x04\x42OLD\x10\x00\x12\n\n\x06ITALIC\x10\x01\"(\n\x05\x43olor\x12\t\n\x01r\x18\x01 \x01(\r\x12\t\n\x01g\x18\x02 \x01(\r\x12\t\n\x01\x62\x18\x03 \x01(\r\"=\n\x0b\x42oundingBox\x12\n\n\x02x1\x18\x01 \x01(\r\x12\n\n\x02y1\x18\x02 \x01(\r\x12\n\n\x02x2\x18\x03 \x01(\r\x12\n\n\x02y2\x18\x04 \x01(\r\",\n\x0e\x43haracterRange\x12\r\n\x05start\x18\x01 \x01(\r\x12\x0b\n\x03\x65nd\x18\x02 \x01(\r\"-\n\x06Header\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.main.CharacterRange\"-\n\x06\x46ooter\x12#\n\x05range\x18\x01 \x01(\x0b\x32\x14.main.CharacterRangeb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recognition_results_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _DOCUMENT._serialized_start=36
  _DOCUMENT._serialized_end=370
  _CHARACTER._serialized_start=372
  _CHARACTER._serialized_end=456
  _PAGE._serialized_start=458
  _PAGE._serialized_end=562
  _TABLE._serialized_start=564
  _TABLE._serialized_end=604
  _TABLECELL._serialized_start=607
  _TABLECELL._serialized_end=820
  _FONT._serialized_start=822
  _FONT._serialized_end=913
  _FONTSIZE._serialized_start=915
  _FONTSIZE._serialized_end=976
  _FONTSTYLE._serialized_start=978
  _FONTSTYLE._serialized_end=1095
  _FONTSTYLE_STYLE._serialized_start=1066
  _FONTSTYLE_STYLE._serialized_end=1095
  _COLOR._serialized_start=1097
  _COLOR._serialized_end=1137
  _BOUNDINGBOX._serialized_start=1139
  _BOUNDINGBOX._serialized_end=1200
  _CHARACTERRANGE._serialized_start=1202
  _CHARACTERRANGE._serialized_end=1246
  _HEADER._serialized_start=1248
  _HEADER._serialized_end=1293
  _FOOTER._serialized_start=1295
  _FOOTER._serialized_end=1340
# @@protoc_insertion_point(module_scope)
