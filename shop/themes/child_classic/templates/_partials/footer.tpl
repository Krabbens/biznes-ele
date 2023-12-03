{**
 * Copyright since 2007 PrestaShop SA and Contributors
 * PrestaShop is an International Registered Trademark & Property of PrestaShop SA
 *
 * NOTICE OF LICENSE
 *
 * This source file is subject to the Academic Free License 3.0 (AFL-3.0)
 * that is bundled with this package in the file LICENSE.md.
 * It is also available through the world-wide-web at this URL:
 * https://opensource.org/licenses/AFL-3.0
 * If you did not receive a copy of the license and are unable to
 * obtain it through the world-wide-web, please send an email
 * to license@prestashop.com so we can send you a copy immediately.
 *
 * DISCLAIMER
 *
 * Do not edit or add to this file if you wish to upgrade PrestaShop to newer
 * versions in the future. If you wish to customize PrestaShop for your
 * needs please refer to https://devdocs.prestashop.com/ for more information.
 *
 * @author    PrestaShop SA and Contributors <contact@prestashop.com>
 * @copyright Since 2007 PrestaShop SA and Contributors
 * @license   https://opensource.org/licenses/AFL-3.0 Academic Free License 3.0 (AFL-3.0)
 *}
<div class="container">
  <div class="row">
    {block name='hook_footer_before'}
      {hook h='displayFooterBefore'}
    {/block}
  </div>
</div>
<div class="footer-container">
  <div class="container">
    <div class="row">
      {block name='hook_footer'}
        {hook h='displayFooter'}
      {/block}
    </div>
    <div class="row">
      {block name='hook_footer_after'}
        {hook h='displayFooterAfter'}
      {/block}
    </div>
  </div>
  <div class="_footer_bottom_1lxga_1">
    <ul class="_legal_menu_1lxga_9" data-auto-id="cms-footer-legal">
      <li class="_legal_menu__item_1lxga_20">
        <a href="/">Ustawienia plików cookies</a>
      </li>
      <li class="_legal_menu__item_1lxga_20">
        <a href="/">Zarządzaj Danymi</a>
      </li>
      <li class="_legal_menu__item_1lxga_20">
        <a href="/">Centrum Prywatności</a>
      </li>
      <li class="_legal_menu__item_1lxga_20">
        <a href="/">Cookies</a>
      </li>
      <li class="_legal_menu__item_1lxga_20">
        <a href="/">Polityka prywatności</a>
      </li>
      <li class="_legal_menu__item_1lxga_20">
        <a href="/">Regulamin</a>
      </li>
    </ul>
  </div>
</div>
