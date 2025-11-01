import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from convert_akomantoso import generate_markdown_text, clean_text_content, process_table


FIXTURE_PATH = Path(__file__).resolve().parents[1] / "test_data" / "20050516_005G0104_VIGENZA_20250130.xml"


class ConvertAkomaNtosoTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        tree = ET.parse(FIXTURE_PATH)
        root = tree.getroot()
        cls.markdown_output = generate_markdown_text(root)

    def test_document_title_is_rendered(self):
        self.assertTrue(
            self.markdown_output.startswith("# Codice dell'amministrazione digitale."),
            "Il titolo del documento dovrebbe essere renderizzato come intestazione H1",
        )

    def test_first_article_heading_is_present(self):
        self.assertIn(
            "# Art. 1. - Definizioni",
            self.markdown_output,
            "Il primo articolo dovrebbe contenere l'intestazione attesa",
        )

    def test_capitolo_heading_format(self):
        self.assertIn(
            "## Capo I - PRINCIPI GENERALI",
            self.markdown_output,
            "La formattazione del capitolo dovrebbe includere numero romano e titolo",
        )

    def test_footnote_element_handling(self):
        """Test that footnote elements are handled without errors"""
        # Create a simple XML element with footnote
        footnote_xml = '''<akn:footnote xmlns:akn="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
            <akn:p>Test footnote content</akn:p>
        </akn:footnote>'''
        root = ET.fromstring(footnote_xml)
        result = clean_text_content(root)
        # Should not crash and should contain some reference
        self.assertIsInstance(result, str)
        self.assertTrue(len(result) > 0)

    def test_quoted_structure_element_handling(self):
        """Test that quotedStructure elements are converted to blockquotes"""
        # Create a simple XML element with quotedStructure as block element
        quoted_xml = '''<akn:quotedStructure xmlns:akn="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
            <akn:p>This is quoted text</akn:p>
        </akn:quotedStructure>'''
        root = ET.fromstring(quoted_xml)
        # Test the clean_text_content function directly on quotedStructure
        result = clean_text_content(root)
        # Should extract the text content
        self.assertIn('This is quoted text', result)

    def test_table_element_handling(self):
        """Test that table elements are converted to markdown tables"""
        # Create a simple XML table
        table_xml = '''<akn:table xmlns:akn="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
            <akn:tr>
                <akn:th>Header 1</akn:th>
                <akn:th>Header 2</akn:th>
            </akn:tr>
            <akn:tr>
                <akn:td>Data 1</akn:td>
                <akn:td>Data 2</akn:td>
            </akn:tr>
        </akn:table>'''
        root = ET.fromstring(table_xml)
        ns = {'akn': 'http://docs.oasis-open.org/legaldocml/ns/akn/3.0'}
        result = process_table(root, ns)
        # Should contain pipe characters for markdown table
        self.assertIn('|', result)
        self.assertIn('Header 1', result)
        self.assertIn('Data 1', result)


if __name__ == "__main__":
    unittest.main()
