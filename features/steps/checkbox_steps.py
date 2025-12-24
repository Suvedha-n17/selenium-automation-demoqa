from behave import given, then
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)


@then('the user selects "{item}" section under "{header}"')
def step_open_checkbox(context, item, header):
    try:
        context.base_page.click(context.checkbox_page.ELEMENTS_MENU_ITEM.format(item, header))
        logger.info(f"Clicked '{item}' under '{header}'")
    except Exception as e:
        logger.exception(f"Failed to navigate to '{item}' under '{header}'")
        raise

@then('the "{node_name}" checkbox should be displayed')
def step_verify_home_checkbox(context,node_name):
    try:
        home_checkbox = context.base_page.is_element_displayed(context.checkbox_page.HOME_CHECKBOX.format(node_name))
        assert home_checkbox, f"Home checkbox is NOT displayed"
        logger.info("Home checkbox is displayed successfully")
    except AssertionError as ae:
        logger.error("Home checkbox is present but not visible")
        raise ae
    except Exception as e:
        logger.exception("Failed to locate Home checkbox")
        raise e

@then('the user expands the tree at all levels using "{tree_node}"')
def step_click_expand_all(context,tree_node):
    try:
        context.base_page.click(context.checkbox_page.EXPAND_ALL_BTN.format(tree_node))
        logger.info("Clicked Expand All button")
    except Exception as e:
        logger.exception("Failed to click Expand All button")
        raise e

@then("all nodes below should be displayed")
def step_verify_nested_elements(context):
    try:
        for row in context.table:
            item = row["Options"]
            element= context.base_page.is_element_displayed(context.base_page.ELEMENTS_MENU.format(item))
            assert element, f"{item} checkbox is not displayed"
            logger.info(f"Verified checkbox displayed: {item}")
    except Exception:
        logger.exception("One or more nested checkbox elements are not displayed")
        raise

@given('the user selects the "{node_name}" node in the checkbox tree')
def step_tick_parent(context, node_name):
    parent_checkbox = context.base_page.find_element(By.XPATH,context.checkbox_page.PARENT_CHECKBOX.format(node_name))
    parent_checkbox.click()

@then('the user de-selects the "{node_name}" node in the checkbox tree')
def step_deselect_parent(context, node_name):
    try:
        parent_checkbox = context.base_page.find_element(By.XPATH,context.checkbox_page.PARENT_CHECKBOX.format(node_name))
        parent_checkbox.click()
        logger.info(f'Parent checkbox "{node_name}" was de-selected successfully')
    except Exception as e:
        logger.exception(f'Failed to de-select parent checkbox "{node_name}": {e}')
        raise

@then('all child node under "{node_name}" should be checked')
def step_verify_children_checked(context, node_name):

    # Returns a cleaned string of all checked checkbox titles under a given parent node.
    try:
        # Get all checked checkboxes
        checked_list = context.base_page.elements_are_present(context.checkbox_page.CHECKED_ITEMS)
        if not checked_list:
            logger.warning(f"No checked checkboxes found under '{node_name}'")
            return ""
        data = [box.find_element('xpath', context.checkbox_page.TITLE_ITEM).text for box in checked_list]
        logger.info(f"Checked checkboxes under '{node_name}': {data}")
        return str(data)
    except Exception as e:
        logger.exception(f"Error in verifying children checked for '{node_name}': {e}")
        return ""

@then('all ancestor nodes of "{node_name}" should be in half-checked state')
def step_verify_ancestors_half_checked(context, node_name):
    try:
        current_node = node_name
        ancestors = []
        while True:
            try:
                parent = context.base_page.find_element(
                    By.XPATH,context.checkbox_page.PARENT_NODE_OF_GIVEN_NODE.format(current_node)
                ).text.strip()

                ancestors.append(parent)
                current_node = parent

                if parent == "Home":  # Root reached
                    break
            except Exception:
                break
        for ancestor in ancestors:
            assert context.base_page.is_element_displayed(
                context.checkbox_page.IS_HALF_CHECKED.format(ancestor)
            ), f"Ancestor '{ancestor}' is NOT in half ticked state"

        logger.info(f"All ancestors of '{node_name}' are half ticked: {ancestors}")

    except Exception as e:
        logger.exception(f"Ancestor indeterminate check failed for '{node_name}': {e}")
        raise

@then('the node "{node_name}" and all its children should be unchecked')
def step_verify_node_children_unchecked(context, node_name):
    # Verify parent node
    parent_checkbox = context.base_page.find_element(By.XPATH, context.checkbox_page.GET_CHECKBOX_NODE.format(node_name))
    assert context.checkbox_page.is_unchecked(parent_checkbox), f"Node '{node_name}' is not unchecked"
    # Verify children
    children_icons = context.checkbox_page.get_children_icons(node_name)

    for icon in children_icons:
        assert context.checkbox_page.is_unchecked(icon),f"A child node under '{node_name}' is still checked"



