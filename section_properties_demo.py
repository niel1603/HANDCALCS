from utils.sections.enum import SectionKey, SourceKey
from utils.sections.registry import SectionRegistry
from utils.sections.properties import SteelSection


registry = SectionRegistry()

sec : SteelSection = registry.get(SectionKey.C_150x65x20x3_2, SourceKey.CNP_GRP)

print(sec.props.Ix)