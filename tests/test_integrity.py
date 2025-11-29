import unittest
import os
import yaml
import toml
import glob

class TestSiteIntegrity(unittest.TestCase):

    def setUp(self):
        self.base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def test_config_files_exist(self):
        """Test that critical configuration files exist."""
        config_files = [
            'config/_default/config.yaml',
            'config/_default/params.yaml',
            'config/_default/menus.yaml',
            'config/_default/languages.yaml'
        ]
        for f in config_files:
            filepath = os.path.join(self.base_dir, f)
            self.assertTrue(os.path.exists(filepath), f"Missing config file: {f}")

    def test_config_yaml_validity(self):
        """Test that config.yaml is valid YAML."""
        filepath = os.path.join(self.base_dir, 'config/_default/config.yaml')
        with open(filepath, 'r') as f:
            try:
                yaml.safe_load(f)
            except yaml.YAMLError as exc:
                self.fail(f"config.yaml is invalid YAML: {exc}")

    def test_admin_author_exists(self):
        """Test that the admin author profile exists."""
        filepath = os.path.join(self.base_dir, 'content/authors/admin/_index.md')
        self.assertTrue(os.path.exists(filepath), "Admin author profile missing at content/authors/admin/_index.md")

    def parse_frontmatter(self, filepath):
        """Helper to parse frontmatter from a markdown file."""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if content.startswith('---'):
            # YAML frontmatter
            try:
                parts = content.split('---', 2)
                if len(parts) >= 3:
                    return yaml.safe_load(parts[1])
                else:
                    print(f"Warning: File {filepath} starts with --- but doesn't seem to have valid YAML frontmatter blocks.")
            except yaml.YAMLError as e:
                self.fail(f"Failed to parse YAML frontmatter in {filepath}: {e}")
        elif content.startswith('+++'):
            # TOML frontmatter
            try:
                parts = content.split('+++', 2)
                if len(parts) >= 3:
                    return toml.loads(parts[1])
                else:
                    print(f"Warning: File {filepath} starts with +++ but doesn't seem to have valid TOML frontmatter blocks.")
            except toml.TomlDecodeError as e:
                self.fail(f"Failed to parse TOML frontmatter in {filepath}: {e}")
        return None

    def test_admin_author_superuser(self):
        """Test that the admin author is a superuser."""
        filepath = os.path.join(self.base_dir, 'content/authors/admin/_index.md')
        data = self.parse_frontmatter(filepath)
        self.assertIsNotNone(data, "Could not parse frontmatter for admin author")
        self.assertTrue(data.get('superuser', False), "Admin author must have 'superuser: true'")

    def test_content_files_have_titles(self):
        """Test that all markdown content files have a title."""
        content_dir = os.path.join(self.base_dir, 'content')
        md_files = glob.glob(os.path.join(content_dir, '**/*.md'), recursive=True)

        for filepath in md_files:
            # Skip _index.md files if they are just directories (though usually they should have titles too)
            # But let's check all for now.
            data = self.parse_frontmatter(filepath)
            if data:
                # Some system files might not have a title but use other mechanisms
                if 'title' not in data:
                    # Allow missing title if it is excluded from CMS or build
                    if data.get('cms_exclude') or data.get('_build', {}).get('render') == 'never':
                        continue
                    # Allow missing title for Wowchemy CMS admin page
                    if data.get('type') == 'wowchemycms':
                        continue
                    self.fail(f"File missing title: {filepath}")

if __name__ == '__main__':
    unittest.main()
