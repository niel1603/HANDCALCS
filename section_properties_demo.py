from utils.sections.enum import SectionKey, SourceKey
from utils.sections.registry import SectionRegistry
from utils.sections.properties import SteelSection


registry = SectionRegistry()

sec : SteelSection = registry.get(SectionKey.WF_150x75x5x7, SourceKey.WF_GRP)

print(sec.props.Ix)




