# Copyright 2015-2016, Tresys Technology, LLC
#
# This file is part of SETools.
#
# SETools is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# SETools is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with SETools.  If not, see <http://www.gnu.org/licenses/>.
#
import unittest

from setools import SELinuxPolicy, PolicyDifference

from .mixins import ValidateRule


class PolicyDifferenceTest(ValidateRule, unittest.TestCase):

    """Policy difference tests."""

    def setUp(self):
        self.diff = PolicyDifference(SELinuxPolicy("tests/diff_left.conf"),
                                     SELinuxPolicy("tests/diff_right.conf"))

    #
    # Types
    #
    def test_added_types(self):
        """Diff: added type"""
        self.assertSetEqual(set(["added_type"]), self.diff.added_types)

    def test_removed_types(self):
        """Diff: modified type"""
        self.assertSetEqual(set(["removed_type"]), self.diff.removed_types)

    def test_modified_types_count(self):
        """Diff: total modified types"""
        self.assertEqual(6, len(self.diff.modified_types))

    def test_modified_types_remove_attr(self):
        """Diff: modified type with removed attribute."""
        self.assertIn("modified_remove_attr", self.diff.modified_types)
        removed_attrs = self.diff.modified_types["modified_remove_attr"].removed_attributes
        self.assertSetEqual(set(["an_attr"]), removed_attrs)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].added_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].matched_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].modified_permissive)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].permissive)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].added_aliases)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].removed_aliases)
        self.assertFalse(self.diff.modified_types["modified_remove_attr"].matched_aliases)

    def test_modified_types_remove_alias(self):
        """Diff: modified type with removed alias."""
        self.assertIn("modified_remove_alias", self.diff.modified_types)
        removed_alias = self.diff.modified_types["modified_remove_alias"].removed_aliases
        self.assertSetEqual(set(["an_alias"]), removed_alias)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].added_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].removed_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].matched_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].modified_permissive)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].permissive)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].added_aliases)
        self.assertFalse(self.diff.modified_types["modified_remove_alias"].matched_aliases)

    def test_modified_types_remove_permissive(self):
        """Diff: modified type with removed permissve."""
        self.assertIn("modified_remove_permissive", self.diff.modified_types)
        self.assertFalse(self.diff.modified_types["modified_remove_permissive"].added_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_permissive"].removed_attributes)
        self.assertFalse(self.diff.modified_types["modified_remove_permissive"].matched_attributes)
        self.assertTrue(self.diff.modified_types["modified_remove_permissive"].modified_permissive)
        self.assertTrue(self.diff.modified_types["modified_remove_permissive"].permissive)
        self.assertFalse(self.diff.modified_types["modified_remove_permissive"].added_aliases)
        self.assertFalse(self.diff.modified_types["modified_remove_permissive"].removed_aliases)
        self.assertFalse(self.diff.modified_types["modified_remove_permissive"].matched_aliases)

    def test_modified_types_add_attr(self):
        """Diff: modified type with added attribute."""
        self.assertIn("modified_add_attr", self.diff.modified_types)
        added_attrs = self.diff.modified_types["modified_add_attr"].added_attributes
        self.assertSetEqual(set(["an_attr"]), added_attrs)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].removed_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].matched_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].modified_permissive)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].permissive)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].added_aliases)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].removed_aliases)
        self.assertFalse(self.diff.modified_types["modified_add_attr"].matched_aliases)

    def test_modified_types_add_alias(self):
        """Diff: modified type with added alias."""
        self.assertIn("modified_add_alias", self.diff.modified_types)
        added_alias = self.diff.modified_types["modified_add_alias"].added_aliases
        self.assertSetEqual(set(["an_alias"]), added_alias)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].added_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].removed_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].matched_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].modified_permissive)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].permissive)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].removed_aliases)
        self.assertFalse(self.diff.modified_types["modified_add_alias"].matched_aliases)

    def test_modified_types_add_permissive(self):
        """Diff: modified type with added permissive."""
        self.assertIn("modified_add_permissive", self.diff.modified_types)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].added_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].removed_attributes)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].matched_attributes)
        self.assertTrue(self.diff.modified_types["modified_add_permissive"].modified_permissive)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].permissive)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].added_aliases)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].removed_aliases)
        self.assertFalse(self.diff.modified_types["modified_add_permissive"].matched_aliases)

    #
    # Roles
    #
    def test_added_role(self):
        """Diff: added role."""
        self.assertSetEqual(set(["added_role"]), self.diff.added_roles)

    def test_removed_role(self):
        """Diff: removed role."""
        self.assertSetEqual(set(["removed_role"]), self.diff.removed_roles)

    def test_modified_role_count(self):
        """Diff: modified role."""
        self.assertIn("object_r", self.diff.modified_roles)
        self.assertEqual(3, len(self.diff.modified_roles))

    def test_modified_role_add_type(self):
        """Diff: modified role with added type."""
        self.assertSetEqual(set(["system"]),
                            self.diff.modified_roles["modified_add_type"].added_types)
        self.assertFalse(self.diff.modified_roles["modified_add_type"].removed_types)

    def test_modified_role_remove_type(self):
        """Diff: modified role with removed type."""
        self.assertSetEqual(set(["system"]),
                            self.diff.modified_roles["modified_remove_type"].removed_types)
        self.assertFalse(self.diff.modified_roles["modified_remove_type"].added_types)

    #
    # Commons
    #
    def test_added_common(self):
        """Diff: added common."""
        self.assertSetEqual(set(["added_common"]), self.diff.added_commons)

    def test_removed_common(self):
        """Diff: removed common."""
        self.assertSetEqual(set(["removed_common"]), self.diff.removed_commons)

    def test_modified_common_count(self):
        """Diff: modified common count."""
        self.assertEqual(2, len(self.diff.modified_commons))

    def test_modified_common_add_perm(self):
        """Diff: modified common with added perm."""
        self.assertSetEqual(set(["added_perm"]),
                            self.diff.modified_commons["modified_add_perm"].added_perms)
        self.assertFalse(self.diff.modified_commons["modified_add_perm"].removed_perms)

    def test_modified_common_remove_perm(self):
        """Diff: modified common with removed perm."""
        self.assertSetEqual(set(["removed_perm"]),
                            self.diff.modified_commons["modified_remove_perm"].removed_perms)
        self.assertFalse(self.diff.modified_commons["modified_remove_perm"].added_perms)

    #
    # Classes
    #
    def test_added_class(self):
        """Diff: added class."""
        self.assertSetEqual(set(["added_class"]), self.diff.added_classes)

    def test_removed_class(self):
        """Diff: removed class."""
        self.assertSetEqual(set(["removed_class"]), self.diff.removed_classes)

    def test_modified_class_count(self):
        """Diff: modified class count."""
        self.assertEqual(3, len(self.diff.modified_classes))

    def test_modified_class_add_perm(self):
        """Diff: modified class with added perm."""
        self.assertSetEqual(set(["added_perm"]),
                            self.diff.modified_classes["modified_add_perm"].added_perms)
        self.assertFalse(self.diff.modified_classes["modified_add_perm"].removed_perms)

    def test_modified_class_remove_perm(self):
        """Diff: modified class with removed perm."""
        self.assertSetEqual(set(["removed_perm"]),
                            self.diff.modified_classes["modified_remove_perm"].removed_perms)
        self.assertFalse(self.diff.modified_classes["modified_remove_perm"].added_perms)

    def test_modified_class_change_common(self):
        """Diff: modified class due to modified common."""
        self.assertSetEqual(set(["old_com"]),
                            self.diff.modified_classes["modified_change_common"].removed_perms)
        self.assertSetEqual(set(["new_com"]),
                            self.diff.modified_classes["modified_change_common"].added_perms)

    #
    # Allow rules
    #
    def test_added_allow_rules(self):
        """Diff: added allow rules."""
        rules = sorted(self.diff.added_allows)
        self.assertEqual(5, len(rules))

        # added rule with existing types
        self.validate_rule(rules[0], "allow", "added_rule_source", "added_rule_target", "infoflow",
                           set(["med_w"]))

        # added rule with new type
        self.validate_rule(rules[1], "allow", "added_type", "added_type", "infoflow2",
                           set(["med_w"]))

        # rule moved out of a conditional
        self.validate_rule(rules[2], "allow", "move_from_bool", "move_from_bool", "infoflow4",
                           set(["hi_r"]))

        # rule moved into a conditional
        self.validate_rule(rules[3], "allow", "move_to_bool", "move_to_bool", "infoflow4",
                           set(["hi_w"]), cond="move_to_bool_b", cond_block=True)

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[4], "allow", "system", "switch_block", "infoflow6",
                           set(["hi_r"]), cond="switch_block_b", cond_block=False)

    def test_removed_allow_rules(self):
        """Diff: removed allow rules."""
        rules = sorted(self.diff.removed_allows)
        self.assertEqual(5, len(rules))

        # rule moved out of a conditional
        self.validate_rule(rules[0], "allow", "move_from_bool", "move_from_bool", "infoflow4",
                           set(["hi_r"]), cond="move_from_bool_b", cond_block=True)

        # rule moved into a conditional
        self.validate_rule(rules[1], "allow", "move_to_bool", "move_to_bool", "infoflow4",
                           set(["hi_w"]))

        # removed rule with existing types
        self.validate_rule(rules[2], "allow", "removed_rule_source", "removed_rule_target",
                           "infoflow", set(["hi_r"]))

        # removed rule with new type
        self.validate_rule(rules[3], "allow", "removed_type", "removed_type", "infoflow3",
                           set(["null"]))

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[4], "allow", "system", "switch_block", "infoflow6",
                           set(["hi_r"]), cond="switch_block_b", cond_block=True)

    def test_modified_allow_rules(self):
        """Diff: modified allow rules."""
        l = sorted(self.diff.modified_allows)
        self.assertEqual(3, len(l))

        # add permissions
        rule, added_perms, removed_perms, matched_perms = l[0]
        self.assertEqual("allow", rule.ruletype)
        self.assertEqual("modified_rule_add_perms", rule.source)
        self.assertEqual("modified_rule_add_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertSetEqual(set(["hi_w"]), added_perms)
        self.assertFalse(removed_perms)
        self.assertSetEqual(set(["hi_r"]), matched_perms)

        # add and remove permissions
        rule, added_perms, removed_perms, matched_perms = l[1]
        self.assertEqual("allow", rule.ruletype)
        self.assertEqual("modified_rule_add_remove_perms", rule.source)
        self.assertEqual("modified_rule_add_remove_perms", rule.target)
        self.assertEqual("infoflow2", rule.tclass)
        self.assertSetEqual(set(["super_r"]), added_perms)
        self.assertSetEqual(set(["super_w"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

        # remove permissions
        rule, added_perms, removed_perms, matched_perms = l[2]
        self.assertEqual("allow", rule.ruletype)
        self.assertEqual("modified_rule_remove_perms", rule.source)
        self.assertEqual("modified_rule_remove_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertFalse(added_perms)
        self.assertSetEqual(set(["low_r"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

    #
    # Auditallow rules
    #
    def test_added_auditallow_rules(self):
        """Diff: added auditallow rules."""
        rules = sorted(self.diff.added_auditallows)
        self.assertEqual(5, len(rules))

        # added rule with existing types
        self.validate_rule(rules[0], "auditallow", "aa_added_rule_source", "aa_added_rule_target",
                           "infoflow", set(["med_w"]))

        # rule moved out of a conditional
        self.validate_rule(rules[1], "auditallow", "aa_move_from_bool", "aa_move_from_bool",
                           "infoflow4", set(["hi_r"]))

        # rule moved into a conditional
        self.validate_rule(rules[2], "auditallow", "aa_move_to_bool", "aa_move_to_bool",
                           "infoflow4", set(["hi_w"]), cond="aa_move_to_bool_b", cond_block=True)

        # added rule with new type
        self.validate_rule(rules[3], "auditallow", "added_type", "added_type", "infoflow7",
                           set(["super_none"]))

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[4], "auditallow", "system", "aa_switch_block", "infoflow6",
                           set(["hi_r"]), cond="aa_switch_block_b", cond_block=False)

    def test_removed_auditallow_rules(self):
        """Diff: removed auditallow rules."""
        rules = sorted(self.diff.removed_auditallows)
        self.assertEqual(5, len(rules))

        # rule moved out of a conditional
        self.validate_rule(rules[0], "auditallow", "aa_move_from_bool", "aa_move_from_bool",
                           "infoflow4", set(["hi_r"]), cond="aa_move_from_bool_b", cond_block=True)

        # rule moved into a conditional
        self.validate_rule(rules[1], "auditallow", "aa_move_to_bool", "aa_move_to_bool",
                           "infoflow4", set(["hi_w"]))

        # removed rule with existing types
        self.validate_rule(rules[2], "auditallow", "aa_removed_rule_source",
                           "aa_removed_rule_target", "infoflow", set(["hi_r"]))

        # removed rule with new type
        self.validate_rule(rules[3], "auditallow", "removed_type", "removed_type", "infoflow7",
                           set(["super_unmapped"]))

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[4], "auditallow", "system", "aa_switch_block", "infoflow6",
                           set(["hi_r"]), cond="aa_switch_block_b", cond_block=True)

    def test_modified_auditallow_rules(self):
        """Diff: modified auditallow rules."""
        l = sorted(self.diff.modified_auditallows)
        self.assertEqual(3, len(l))

        # add permissions
        rule, added_perms, removed_perms, matched_perms = l[0]
        self.assertEqual("auditallow", rule.ruletype)
        self.assertEqual("aa_modified_rule_add_perms", rule.source)
        self.assertEqual("aa_modified_rule_add_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertSetEqual(set(["hi_w"]), added_perms)
        self.assertFalse(removed_perms)
        self.assertSetEqual(set(["hi_r"]), matched_perms)

        # add and remove permissions
        rule, added_perms, removed_perms, matched_perms = l[1]
        self.assertEqual("auditallow", rule.ruletype)
        self.assertEqual("aa_modified_rule_add_remove_perms", rule.source)
        self.assertEqual("aa_modified_rule_add_remove_perms", rule.target)
        self.assertEqual("infoflow2", rule.tclass)
        self.assertSetEqual(set(["super_r"]), added_perms)
        self.assertSetEqual(set(["super_w"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

        # remove permissions
        rule, added_perms, removed_perms, matched_perms = l[2]
        self.assertEqual("auditallow", rule.ruletype)
        self.assertEqual("aa_modified_rule_remove_perms", rule.source)
        self.assertEqual("aa_modified_rule_remove_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertFalse(added_perms)
        self.assertSetEqual(set(["low_r"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

    #
    # Dontaudit rules
    #
    def test_added_dontaudit_rules(self):
        """Diff: added dontaudit rules."""
        rules = sorted(self.diff.added_dontaudits)
        self.assertEqual(5, len(rules))

        # added rule with new type
        self.validate_rule(rules[0], "dontaudit", "added_type", "added_type", "infoflow7",
                           set(["super_none"]))

        # added rule with existing types
        self.validate_rule(rules[1], "dontaudit", "da_added_rule_source", "da_added_rule_target",
                           "infoflow", set(["med_w"]))

        # rule moved out of a conditional
        self.validate_rule(rules[2], "dontaudit", "da_move_from_bool", "da_move_from_bool",
                           "infoflow4", set(["hi_r"]))

        # rule moved into a conditional
        self.validate_rule(rules[3], "dontaudit", "da_move_to_bool", "da_move_to_bool",
                           "infoflow4", set(["hi_w"]), cond="da_move_to_bool_b", cond_block=True)

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[4], "dontaudit", "system", "da_switch_block", "infoflow6",
                           set(["hi_r"]), cond="da_switch_block_b", cond_block=False)

    def test_removed_dontaudit_rules(self):
        """Diff: removed dontaudit rules."""
        rules = sorted(self.diff.removed_dontaudits)
        self.assertEqual(5, len(rules))

        # rule moved out of a conditional
        self.validate_rule(rules[0], "dontaudit", "da_move_from_bool", "da_move_from_bool",
                           "infoflow4", set(["hi_r"]), cond="da_move_from_bool_b", cond_block=True)

        # rule moved into a conditional
        self.validate_rule(rules[1], "dontaudit", "da_move_to_bool", "da_move_to_bool",
                           "infoflow4", set(["hi_w"]))

        # removed rule with existing types
        self.validate_rule(rules[2], "dontaudit", "da_removed_rule_source",
                           "da_removed_rule_target", "infoflow", set(["hi_r"]))

        # removed rule with new type
        self.validate_rule(rules[3], "dontaudit", "removed_type", "removed_type", "infoflow7",
                           set(["super_both"]))

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[4], "dontaudit", "system", "da_switch_block", "infoflow6",
                           set(["hi_r"]), cond="da_switch_block_b", cond_block=True)

    def test_modified_dontaudit_rules(self):
        """Diff: modified dontaudit rules."""
        l = sorted(self.diff.modified_dontaudits)
        self.assertEqual(3, len(l))

        # add permissions
        rule, added_perms, removed_perms, matched_perms = l[0]
        self.assertEqual("dontaudit", rule.ruletype)
        self.assertEqual("da_modified_rule_add_perms", rule.source)
        self.assertEqual("da_modified_rule_add_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertSetEqual(set(["hi_w"]), added_perms)
        self.assertFalse(removed_perms)
        self.assertSetEqual(set(["hi_r"]), matched_perms)

        # add and remove permissions
        rule, added_perms, removed_perms, matched_perms = l[1]
        self.assertEqual("dontaudit", rule.ruletype)
        self.assertEqual("da_modified_rule_add_remove_perms", rule.source)
        self.assertEqual("da_modified_rule_add_remove_perms", rule.target)
        self.assertEqual("infoflow2", rule.tclass)
        self.assertSetEqual(set(["super_r"]), added_perms)
        self.assertSetEqual(set(["super_w"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

        # remove permissions
        rule, added_perms, removed_perms, matched_perms = l[2]
        self.assertEqual("dontaudit", rule.ruletype)
        self.assertEqual("da_modified_rule_remove_perms", rule.source)
        self.assertEqual("da_modified_rule_remove_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertFalse(added_perms)
        self.assertSetEqual(set(["low_r"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

    #
    # Neverallow rules
    #
    def test_added_neverallow_rules(self):
        """Diff: added neverallow rules."""
        rules = sorted(self.diff.added_neverallows)
        self.assertEqual(2, len(rules))

        # added rule with new type
        self.validate_rule(rules[0], "neverallow", "added_type", "added_type", "added_class",
                           set(["new_class_perm"]))

        # added rule with existing types
        self.validate_rule(rules[1], "neverallow", "na_added_rule_source", "na_added_rule_target",
                           "infoflow", set(["med_w"]))

    def test_removed_neverallow_rules(self):
        """Diff: removed neverallow rules."""
        rules = sorted(self.diff.removed_neverallows)
        self.assertEqual(2, len(rules))

        # removed rule with existing types
        self.validate_rule(rules[0], "neverallow", "na_removed_rule_source",
                           "na_removed_rule_target", "infoflow", set(["hi_r"]))

        # removed rule with new type
        self.validate_rule(rules[1], "neverallow", "removed_type", "removed_type", "removed_class",
                           set(["null_perm"]))

    def test_modified_neverallow_rules(self):
        """Diff: modified neverallow rules."""
        l = sorted(self.diff.modified_neverallows)
        self.assertEqual(3, len(l))

        # add permissions
        rule, added_perms, removed_perms, matched_perms = l[0]
        self.assertEqual("neverallow", rule.ruletype)
        self.assertEqual("na_modified_rule_add_perms", rule.source)
        self.assertEqual("na_modified_rule_add_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertSetEqual(set(["hi_w"]), added_perms)
        self.assertFalse(removed_perms)
        self.assertSetEqual(set(["hi_r"]), matched_perms)

        # add and remove permissions
        rule, added_perms, removed_perms, matched_perms = l[1]
        self.assertEqual("neverallow", rule.ruletype)
        self.assertEqual("na_modified_rule_add_remove_perms", rule.source)
        self.assertEqual("na_modified_rule_add_remove_perms", rule.target)
        self.assertEqual("infoflow2", rule.tclass)
        self.assertSetEqual(set(["super_r"]), added_perms)
        self.assertSetEqual(set(["super_w"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

        # remove permissions
        rule, added_perms, removed_perms, matched_perms = l[2]
        self.assertEqual("neverallow", rule.ruletype)
        self.assertEqual("na_modified_rule_remove_perms", rule.source)
        self.assertEqual("na_modified_rule_remove_perms", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertFalse(added_perms)
        self.assertSetEqual(set(["low_r"]), removed_perms)
        self.assertSetEqual(set(["low_w"]), matched_perms)

    #
    # Type_transition rules
    #
    def test_added_type_transition_rules(self):
        """Diff: added type_transition rules."""
        rules = sorted(self.diff.added_type_transitions)
        self.assertEqual(5, len(rules))

        # added rule with new type
        self.validate_rule(rules[0], "type_transition", "added_type", "system", "infoflow4",
                           "system")

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[1], "type_transition", "system", "tt_switch_block", "infoflow6",
                           "system", cond="tt_switch_block_b", cond_block=False)

        # added rule with existing types
        self.validate_rule(rules[2], "type_transition", "tt_added_rule_source",
                           "tt_added_rule_target", "infoflow", "system")

        # rule moved out of a conditional
        self.validate_rule(rules[3], "type_transition", "tt_move_from_bool", "system",
                           "infoflow4", "system")

        # rule moved into a conditional
        self.validate_rule(rules[4], "type_transition", "tt_move_to_bool", "system",
                           "infoflow3", "system", cond="tt_move_to_bool_b", cond_block=True)

    def test_removed_type_transition_rules(self):
        """Diff: removed type_transition rules."""
        rules = sorted(self.diff.removed_type_transitions)
        self.assertEqual(5, len(rules))

        # removed rule with new type
        self.validate_rule(rules[0], "type_transition", "removed_type", "system", "infoflow4",
                           "system")

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[1], "type_transition", "system", "tt_switch_block", "infoflow6",
                           "system", cond="tt_switch_block_b", cond_block=True)

        # rule moved out of a conditional
        self.validate_rule(rules[2], "type_transition", "tt_move_from_bool", "system",
                           "infoflow4", "system", cond="tt_move_from_bool_b", cond_block=True)

        # rule moved into a conditional
        self.validate_rule(rules[3], "type_transition", "tt_move_to_bool", "system",
                           "infoflow3", "system")

        # removed rule with existing types
        self.validate_rule(rules[4], "type_transition", "tt_removed_rule_source",
                           "tt_removed_rule_target", "infoflow", "system")

    def test_modified_type_transition_rules(self):
        """Diff: modified type_transition rules."""
        l = sorted(self.diff.modified_type_transitions)
        self.assertEqual(1, len(l))

        rule, added_default, removed_default = l[0]
        self.assertEqual("type_transition", rule.ruletype)
        self.assertEqual("tt_matched_source", rule.source)
        self.assertEqual("system", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertEqual("tt_new_type", added_default)
        self.assertEqual("tt_old_type", removed_default)

    #
    # Type_change rules
    #
    def test_added_type_change_rules(self):
        """Diff: added type_change rules."""
        rules = sorted(self.diff.added_type_changes)
        self.assertEqual(5, len(rules))

        # added rule with new type
        self.validate_rule(rules[0], "type_change", "added_type", "system", "infoflow4",
                           "system")

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[1], "type_change", "system", "tc_switch_block", "infoflow6",
                           "system", cond="tc_switch_block_b", cond_block=False)

        # added rule with existing types
        self.validate_rule(rules[2], "type_change", "tc_added_rule_source",
                           "tc_added_rule_target", "infoflow", "system")

        # rule moved out of a conditional
        self.validate_rule(rules[3], "type_change", "tc_move_from_bool", "system",
                           "infoflow4", "system")

        # rule moved into a conditional
        self.validate_rule(rules[4], "type_change", "tc_move_to_bool", "system",
                           "infoflow3", "system", cond="tc_move_to_bool_b", cond_block=True)

    def test_removed_type_change_rules(self):
        """Diff: removed type_change rules."""
        rules = sorted(self.diff.removed_type_changes)
        self.assertEqual(5, len(rules))

        # removed rule with new type
        self.validate_rule(rules[0], "type_change", "removed_type", "system", "infoflow4",
                           "system")

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[1], "type_change", "system", "tc_switch_block", "infoflow6",
                           "system", cond="tc_switch_block_b", cond_block=True)

        # rule moved out of a conditional
        self.validate_rule(rules[2], "type_change", "tc_move_from_bool", "system",
                           "infoflow4", "system", cond="tc_move_from_bool_b", cond_block=True)

        # rule moved into a conditional
        self.validate_rule(rules[3], "type_change", "tc_move_to_bool", "system",
                           "infoflow3", "system")

        # removed rule with existing types
        self.validate_rule(rules[4], "type_change", "tc_removed_rule_source",
                           "tc_removed_rule_target", "infoflow", "system")

    def test_modified_type_change_rules(self):
        """Diff: modified type_change rules."""
        l = sorted(self.diff.modified_type_changes)
        self.assertEqual(1, len(l))

        rule, added_default, removed_default = l[0]
        self.assertEqual("type_change", rule.ruletype)
        self.assertEqual("tc_matched_source", rule.source)
        self.assertEqual("system", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertEqual("tc_new_type", added_default)
        self.assertEqual("tc_old_type", removed_default)

    #
    # Type_member rules
    #
    def test_added_type_member_rules(self):
        """Diff: added type_member rules."""
        rules = sorted(self.diff.added_type_members)
        self.assertEqual(5, len(rules))

        # added rule with new type
        self.validate_rule(rules[0], "type_member", "added_type", "system", "infoflow4",
                           "system")

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[1], "type_member", "system", "tm_switch_block", "infoflow6",
                           "system", cond="tm_switch_block_b", cond_block=False)

        # added rule with existing types
        self.validate_rule(rules[2], "type_member", "tm_added_rule_source",
                           "tm_added_rule_target", "infoflow", "system")

        # rule moved out of a conditional
        self.validate_rule(rules[3], "type_member", "tm_move_from_bool", "system",
                           "infoflow4", "system")

        # rule moved into a conditional
        self.validate_rule(rules[4], "type_member", "tm_move_to_bool", "system",
                           "infoflow3", "system", cond="tm_move_to_bool_b", cond_block=True)

    def test_removed_type_member_rules(self):
        """Diff: removed type_member rules."""
        rules = sorted(self.diff.removed_type_members)
        self.assertEqual(5, len(rules))

        # removed rule with new type
        self.validate_rule(rules[0], "type_member", "removed_type", "system", "infoflow4",
                           "system")

        # rule moved from one conditional block to another (true to false)
        self.validate_rule(rules[1], "type_member", "system", "tm_switch_block", "infoflow6",
                           "system", cond="tm_switch_block_b", cond_block=True)

        # rule moved out of a conditional
        self.validate_rule(rules[2], "type_member", "tm_move_from_bool", "system",
                           "infoflow4", "system", cond="tm_move_from_bool_b", cond_block=True)

        # rule moved into a conditional
        self.validate_rule(rules[3], "type_member", "tm_move_to_bool", "system",
                           "infoflow3", "system")

        # removed rule with existing types
        self.validate_rule(rules[4], "type_member", "tm_removed_rule_source",
                           "tm_removed_rule_target", "infoflow", "system")

    def test_modified_type_member_rules(self):
        """Diff: modified type_member rules."""
        l = sorted(self.diff.modified_type_members)
        self.assertEqual(1, len(l))

        rule, added_default, removed_default = l[0]
        self.assertEqual("type_member", rule.ruletype)
        self.assertEqual("tm_matched_source", rule.source)
        self.assertEqual("system", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertEqual("tm_new_type", added_default)
        self.assertEqual("tm_old_type", removed_default)

    #
    # Range_transition rules
    #
    def test_added_range_transition_rules(self):
        """Diff: added range_transition rules."""
        rules = sorted(self.diff.added_range_transitions)
        self.assertEqual(2, len(rules))

        # added rule with new type
        self.validate_rule(rules[0], "range_transition", "added_type", "system", "infoflow4",
                           "s3")

        # added rule with existing types
        self.validate_rule(rules[1], "range_transition", "rt_added_rule_source",
                           "rt_added_rule_target", "infoflow", "s3")

    def test_removed_range_transition_rules(self):
        """Diff: removed range_transition rules."""
        rules = sorted(self.diff.removed_range_transitions)
        self.assertEqual(2, len(rules))

        # removed rule with new type
        self.validate_rule(rules[0], "range_transition", "removed_type", "system", "infoflow4",
                           "s1")

        # removed rule with existing types
        self.validate_rule(rules[1], "range_transition", "rt_removed_rule_source",
                           "rt_removed_rule_target", "infoflow", "s1")

    def test_modified_range_transition_rules(self):
        """Diff: modified range_transition rules."""
        l = sorted(self.diff.modified_range_transitions)
        self.assertEqual(1, len(l))

        rule, added_default, removed_default = l[0]
        self.assertEqual("range_transition", rule.ruletype)
        self.assertEqual("rt_matched_source", rule.source)
        self.assertEqual("system", rule.target)
        self.assertEqual("infoflow", rule.tclass)
        self.assertEqual("s0:c0,c4 - s1:c0.c2,c4", added_default)
        self.assertEqual("s2:c0 - s3:c0.c2", removed_default)

    #
    # Role allow rules
    #
    def test_added_role_allow_rules(self):
        """Diff: added role_allow rules."""
        rules = sorted(self.diff.added_role_allows)
        self.assertEqual(2, len(rules))

        # added rule with existing roles
        self.assertEqual("allow", rules[0].ruletype)
        self.assertEqual("added_role", rules[0].source)
        self.assertEqual("system", rules[0].target)

        # added rule with new roles
        self.assertEqual("allow", rules[1].ruletype)
        self.assertEqual("added_rule_source_r", rules[1].source)
        self.assertEqual("added_rule_target_r", rules[1].target)

    def test_removed_role_allow_rules(self):
        """Diff: removed role_allow rules."""
        rules = sorted(self.diff.removed_role_allows)
        self.assertEqual(2, len(rules))

        # removed rule with removed role
        self.assertEqual("allow", rules[0].ruletype)
        self.assertEqual("removed_role", rules[0].source)
        self.assertEqual("system", rules[0].target)

        # removed rule with existing roles
        self.assertEqual("allow", rules[1].ruletype)
        self.assertEqual("removed_rule_source_r", rules[1].source)
        self.assertEqual("removed_rule_target_r", rules[1].target)

    #
    # Role_transition rules
    #
    def test_added_role_transition_rules(self):
        """Diff: added role_transition rules."""
        rules = sorted(self.diff.added_role_transitions)
        self.assertEqual(2, len(rules))

        # added rule with new role
        self.validate_rule(rules[0], "role_transition", "added_role", "system", "infoflow4",
                           "system")

        # added rule with existing roles
        self.validate_rule(rules[1], "role_transition", "role_tr_added_rule_source",
                           "role_tr_added_rule_target", "infoflow6", "system")

    def test_removed_role_transition_rules(self):
        """Diff: removed role_transition rules."""
        rules = sorted(self.diff.removed_role_transitions)
        self.assertEqual(2, len(rules))

        # removed rule with new role
        self.validate_rule(rules[0], "role_transition", "removed_role", "system", "infoflow4",
                           "system")

        # removed rule with existing roles
        self.validate_rule(rules[1], "role_transition", "role_tr_removed_rule_source",
                           "role_tr_removed_rule_target", "infoflow5", "system")

    def test_modified_role_transition_rules(self):
        """Diff: modified role_transition rules."""
        l = sorted(self.diff.modified_role_transitions)
        self.assertEqual(1, len(l))

        rule, added_default, removed_default = l[0]
        self.assertEqual("role_transition", rule.ruletype)
        self.assertEqual("role_tr_matched_source", rule.source)
        self.assertEqual("role_tr_matched_target", rule.target)
        self.assertEqual("infoflow3", rule.tclass)
        self.assertEqual("role_tr_new_role", added_default)
        self.assertEqual("role_tr_old_role", removed_default)

    #
    # Users
    #
    def test_added_user(self):
        """Diff: added user."""
        self.assertSetEqual(set(["added_user"]), self.diff.added_users)

    def test_removed_user(self):
        """Diff: removed user."""
        self.assertSetEqual(set(["removed_user"]), self.diff.removed_users)

    def test_modified_user_count(self):
        """Diff: modified user count."""
        self.assertEqual(4, len(self.diff.modified_users))

    def test_modified_user_add_role(self):
        """Diff: modified user with added role."""
        self.assertSetEqual(set(["added_role"]),
                            self.diff.modified_users["modified_add_role"].added_roles)
        self.assertFalse(self.diff.modified_users["modified_add_role"].removed_roles)

    def test_modified_user_remove_role(self):
        """Diff: modified user with removed role."""
        self.assertSetEqual(set(["removed_role"]),
                            self.diff.modified_users["modified_remove_role"].removed_roles)
        self.assertFalse(self.diff.modified_users["modified_remove_role"].added_roles)

    def test_modified_user_change_level(self):
        """Diff: modified user due to modified default level."""
        self.assertEqual("s2:c0", self.diff.modified_users["modified_change_level"].removed_level)
        self.assertEqual("s2:c1", self.diff.modified_users["modified_change_level"].added_level)

    def test_modified_user_change_range(self):
        """Diff: modified user due to modified range."""
        self.assertEqual("s3:c1.c3",
                         self.diff.modified_users["modified_change_range"].removed_range)
        self.assertEqual("s3:c1.c4",
                         self.diff.modified_users["modified_change_range"].added_range)

    #
    # Type attributes
    #
    def test_added_type_attribute(self):
        """Diff: added type attribute."""
        self.assertSetEqual(set(["added_attr"]), self.diff.added_type_attributes)

    def test_removed_type_attribute(self):
        """Diff: removed type attribute."""
        self.assertSetEqual(set(["removed_attr"]), self.diff.removed_type_attributes)

    def test_modified_type_attribute(self):
        """Diff: modified type attribute."""
        self.assertEqual(1, len(self.diff.modified_type_attributes))
        self.assertSetEqual(set(["modified_add_attr"]),
                            self.diff.modified_type_attributes["an_attr"].added_types)
        self.assertSetEqual(set(["modified_remove_attr"]),
                            self.diff.modified_type_attributes["an_attr"].removed_types)

    #
    # Booleans
    #
    def test_added_boolean(self):
        """Diff: added boolean."""
        self.assertSetEqual(set(["added_bool"]), self.diff.added_booleans)

    def test_removed_boolean(self):
        """Diff: removed boolean."""
        self.assertSetEqual(set(["removed_bool"]), self.diff.removed_booleans)

    def test_modified_boolean(self):
        """Diff: modified boolean."""
        self.assertEqual(1, len(self.diff.modified_booleans))
        self.assertTrue(self.diff.modified_booleans["modified_bool"].added_state)
        self.assertFalse(self.diff.modified_booleans["modified_bool"].removed_state)

    #
    # Categories
    #
    def test_added_category(self):
        """Diff: added category."""
        self.assertSetEqual(set(["c6"]), self.diff.added_categories)

    def test_removed_category(self):
        """Diff: removed category."""
        self.assertSetEqual(set(["c5"]), self.diff.removed_categories)

    def test_modified_category(self):
        """Diff: modified categories."""
        self.assertEqual(2, len(self.diff.modified_categories))

        # add alias
        self.assertEqual(set(["foo"]), self.diff.modified_categories["c1"].added_aliases)
        self.assertFalse(self.diff.modified_categories["c1"].removed_aliases)

        # remove alias
        self.assertFalse(self.diff.modified_categories["c0"].added_aliases)
        self.assertEqual(set(["eggs"]), self.diff.modified_categories["c0"].removed_aliases)

    #
    # Sensitivity
    #
    def test_added_sensitivities(self):
        """Diff: added sensitivities."""
        self.assertSetEqual(set(["s46"]), self.diff.added_sensitivities)

    def test_removed_sensitivities(self):
        """Diff: removed sensitivities."""
        self.assertSetEqual(set(["s47"]), self.diff.removed_sensitivities)

    def test_modified_sensitivities(self):
        """Diff: modified sensitivities."""
        self.assertEqual(2, len(self.diff.modified_sensitivities))

        # add alias
        self.assertSetEqual(set(["al4"]), self.diff.modified_sensitivities["s1"].added_aliases)
        self.assertFalse(self.diff.modified_sensitivities["s1"].removed_aliases)

        # remove alias
        self.assertFalse(self.diff.modified_sensitivities["s0"].added_aliases)
        self.assertSetEqual(set(["al2"]), self.diff.modified_sensitivities["s0"].removed_aliases)

    #
    # Initial SIDs
    #
    def test_added_initialsids(self):
        """Diff: added initialsids."""
        self.assertSetEqual(set(["added_sid"]), self.diff.added_initialsids)

    def test_removed_initialsids(self):
        """Diff: removed initialsids."""
        self.assertSetEqual(set(["removed_sid"]), self.diff.removed_initialsids)

    def test_modified_initialsids(self):
        """Diff: modified initialsids."""
        self.assertEqual(1, len(self.diff.modified_initialsids))
        self.assertEqual("modified_add_role:system:system:s2",
                         self.diff.modified_initialsids["modified_sid"].added_context)
        self.assertEqual("system:system:system:s0",
                         self.diff.modified_initialsids["modified_sid"].removed_context)

    #
    # fs_use_*
    #
    def test_added_fs_uses(self):
        """Diff: added fs_uses."""
        l = sorted(self.diff.added_fs_uses)
        self.assertEqual(1, len(l))

        rule = l[0]
        self.assertEqual("fs_use_xattr", rule.ruletype)
        self.assertEqual("added_fsuse", rule.fs)
        self.assertEqual("system:object_r:system:s0", rule.context)

    def test_removed_fs_uses(self):
        """Diff: removed fs_uses."""
        l = sorted(self.diff.removed_fs_uses)
        self.assertEqual(1, len(l))

        rule = l[0]
        self.assertEqual("fs_use_task", rule.ruletype)
        self.assertEqual("removed_fsuse", rule.fs)
        self.assertEqual("system:object_r:system:s0", rule.context)

    def test_modified_fs_uses(self):
        """Diff: modified fs_uses."""
        l = sorted(self.diff.modified_fs_uses)
        self.assertEqual(1, len(l))

        rule, added_context, removed_context = l[0]
        self.assertEqual("fs_use_trans", rule.ruletype)
        self.assertEqual("modified_fsuse", rule.fs)
        self.assertEqual("added_user:object_r:system:s1", added_context)
        self.assertEqual("removed_user:object_r:system:s0", removed_context)


class PolicyDifferenceTestNoDiff(unittest.TestCase):

    """Policy difference test with no policy differences."""

    def setUp(self):
        self.diff = PolicyDifference(SELinuxPolicy("tests/diff_left.conf"),
                                     SELinuxPolicy("tests/diff_left.conf"))

    def test_added_types(self):
        """NoDiff: no added types"""
        self.assertFalse(self.diff.added_types)

    def test_removed_types(self):
        """NoDiff: no removed types"""
        self.assertFalse(self.diff.removed_types)

    def test_modified_types(self):
        """NoDiff: no modified types"""
        self.assertFalse(self.diff.modified_types)

    def test_added_roles(self):
        """NoDiff: no added roles."""
        self.assertFalse(self.diff.added_roles)

    def test_removed_roles(self):
        """NoDiff: no removed roles."""
        self.assertFalse(self.diff.removed_roles)

    def test_modified_roles(self):
        """NoDiff: no modified roles."""
        self.assertFalse(self.diff.modified_roles)

    def test_added_commons(self):
        """NoDiff: no added commons."""
        self.assertFalse(self.diff.added_commons)

    def test_removed_commons(self):
        """NoDiff: no removed commons."""
        self.assertFalse(self.diff.removed_commons)

    def test_modified_commons(self):
        """NoDiff: no modified commons."""
        self.assertFalse(self.diff.modified_commons)

    def test_added_classes(self):
        """NoDiff: no added classes."""
        self.assertFalse(self.diff.added_classes)

    def test_removed_classes(self):
        """NoDiff: no removed classes."""
        self.assertFalse(self.diff.removed_classes)

    def test_modified_classes(self):
        """NoDiff: no modified classes."""
        self.assertFalse(self.diff.modified_classes)

    def test_added_allows(self):
        """NoDiff: no added allow rules."""
        self.assertFalse(self.diff.added_allows)

    def test_removed_allows(self):
        """NoDiff: no removed allow rules."""
        self.assertFalse(self.diff.removed_allows)

    def test_modified_allows(self):
        """NoDiff: no modified allow rules."""
        self.assertFalse(self.diff.modified_allows)

    def test_added_auditallows(self):
        """NoDiff: no added auditallow rules."""
        self.assertFalse(self.diff.added_auditallows)

    def test_removed_auditallows(self):
        """NoDiff: no removed auditallow rules."""
        self.assertFalse(self.diff.removed_auditallows)

    def test_modified_auditallows(self):
        """NoDiff: no modified auditallow rules."""
        self.assertFalse(self.diff.modified_auditallows)

    def test_added_neverallows(self):
        """NoDiff: no added neverallow rules."""
        self.assertFalse(self.diff.added_neverallows)

    def test_removed_neverallows(self):
        """NoDiff: no removed neverallow rules."""
        self.assertFalse(self.diff.removed_neverallows)

    def test_modified_neverallows(self):
        """NoDiff: no modified neverallow rules."""
        self.assertFalse(self.diff.modified_neverallows)

    def test_added_dontaudits(self):
        """NoDiff: no added dontaudit rules."""
        self.assertFalse(self.diff.added_dontaudits)

    def test_removed_dontaudits(self):
        """NoDiff: no removed dontaudit rules."""
        self.assertFalse(self.diff.removed_dontaudits)

    def test_modified_dontaudits(self):
        """NoDiff: no modified dontaudit rules."""
        self.assertFalse(self.diff.modified_dontaudits)

    def test_added_type_transitions(self):
        """NoDiff: no added type_transition rules."""
        self.assertFalse(self.diff.added_type_transitions)

    def test_removed_type_transitions(self):
        """NoDiff: no removed type_transition rules."""
        self.assertFalse(self.diff.removed_type_transitions)

    def test_modified_type_transitions(self):
        """NoDiff: no modified type_transition rules."""
        self.assertFalse(self.diff.modified_type_transitions)

    def test_added_type_changes(self):
        """NoDiff: no added type_change rules."""
        self.assertFalse(self.diff.added_type_changes)

    def test_removed_type_changes(self):
        """NoDiff: no removed type_change rules."""
        self.assertFalse(self.diff.removed_type_changes)

    def test_modified_type_changes(self):
        """NoDiff: no modified type_change rules."""
        self.assertFalse(self.diff.modified_type_changes)

    def test_added_type_members(self):
        """NoDiff: no added type_member rules."""
        self.assertFalse(self.diff.added_type_members)

    def test_removed_type_members(self):
        """NoDiff: no removed type_member rules."""
        self.assertFalse(self.diff.removed_type_members)

    def test_modified_type_members(self):
        """NoDiff: no modified type_member rules."""
        self.assertFalse(self.diff.modified_type_members)

    def test_added_range_transitions(self):
        """NoDiff: no added range_transition rules."""
        self.assertFalse(self.diff.added_range_transitions)

    def test_removed_range_transitions(self):
        """NoDiff: no removed range_transition rules."""
        self.assertFalse(self.diff.removed_range_transitions)

    def test_modified_range_transitions(self):
        """NoDiff: no modified range_transition rules."""
        self.assertFalse(self.diff.modified_range_transitions)

    def test_added_role_allows(self):
        """NoDiff: no added role_allow rules."""
        self.assertFalse(self.diff.added_role_allows)

    def test_removed_role_allows(self):
        """NoDiff: no removed role_allow rules."""
        self.assertFalse(self.diff.removed_role_allows)

    def test_modified_role_allows(self):
        """NoDiff: no modified role_allow rules."""
        self.assertFalse(self.diff.modified_role_allows)

    def test_added_role_transitions(self):
        """NoDiff: no added role_transition rules."""
        self.assertFalse(self.diff.added_role_transitions)

    def test_removed_role_transitions(self):
        """NoDiff: no removed role_transition rules."""
        self.assertFalse(self.diff.removed_role_transitions)

    def test_modified_role_transitions(self):
        """NoDiff: no modified role_transition rules."""
        self.assertFalse(self.diff.modified_role_transitions)

    def test_added_users(self):
        """NoDiff: no added users."""
        self.assertFalse(self.diff.added_users)

    def test_removed_users(self):
        """NoDiff: no removed users."""
        self.assertFalse(self.diff.removed_users)

    def test_modified_users(self):
        """NoDiff: no modified user rules."""
        self.assertFalse(self.diff.modified_users)

    def test_added_type_attributes(self):
        """NoDiff: no added type attribute."""
        self.assertFalse(self.diff.added_type_attributes)

    def test_removed_type_attributes(self):
        """NoDiff: no removed type attributes."""
        self.assertFalse(self.diff.removed_type_attributes)

    def test_modified_type_attributes(self):
        """NoDiff: no modified type attributes."""
        self.assertFalse(self.diff.modified_type_attributes)

    def test_added_booleans(self):
        """NoDiff: no added booleans."""
        self.assertFalse(self.diff.added_booleans)

    def test_removed_booleans(self):
        """NoDiff: no removed booleans."""
        self.assertFalse(self.diff.removed_booleans)

    def test_modified_booleans(self):
        """NoDiff: no modified booleans."""
        self.assertFalse(self.diff.modified_booleans)

    def test_added_categories(self):
        """NoDiff: no added categories."""
        self.assertFalse(self.diff.added_categories)

    def test_removed_categories(self):
        """NoDiff: no removed categories."""
        self.assertFalse(self.diff.removed_categories)

    def test_modified_categories(self):
        """NoDiff: no modified categories."""
        self.assertFalse(self.diff.modified_categories)

    def test_added_sensitivities(self):
        """NoDiff: no added sensitivities."""
        self.assertFalse(self.diff.added_sensitivities)

    def test_removed_sensitivities(self):
        """NoDiff: no removed sensitivities."""
        self.assertFalse(self.diff.removed_sensitivities)

    def test_modified_sensitivities(self):
        """NoDiff: no modified sensitivities."""
        self.assertFalse(self.diff.modified_sensitivities)

    def test_added_initialsids(self):
        """NoDiff: no added initialsids."""
        self.assertFalse(self.diff.added_initialsids)

    def test_removed_initialsids(self):
        """NoDiff: no removed initialsids."""
        self.assertFalse(self.diff.removed_initialsids)

    def test_modified_initialsids(self):
        """NoDiff: no modified initialsids."""
        self.assertFalse(self.diff.modified_initialsids)

    def test_added_fs_uses(self):
        """NoDiff: no added fs_uses."""
        self.assertFalse(self.diff.added_fs_uses)

    def test_removed_fs_uses(self):
        """NoDiff: no removed fs_uses."""
        self.assertFalse(self.diff.removed_fs_uses)

    def test_modified_fs_uses(self):
        """NoDiff: no modified fs_uses."""
        self.assertFalse(self.diff.modified_fs_uses)
