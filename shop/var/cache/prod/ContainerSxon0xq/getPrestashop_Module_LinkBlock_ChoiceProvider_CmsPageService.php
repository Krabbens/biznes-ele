<?php

use Symfony\Component\DependencyInjection\Argument\RewindableGenerator;

// This file has been auto-generated by the Symfony Dependency Injection Component for internal use.
// Returns the public 'prestashop.module.link_block.choice_provider.cms_page' shared service.

return $this->services['prestashop.module.link_block.choice_provider.cms_page'] = new \PrestaShop\Module\LinkList\Form\ChoiceProvider\CMSPageChoiceProvider(${($_ = isset($this->services['doctrine.dbal.default_connection']) ? $this->services['doctrine.dbal.default_connection'] : $this->getDoctrine_Dbal_DefaultConnectionService()) && false ?: '_'}, 'ad_', ${($_ = isset($this->services['prestashop.module.link_block.choice_provider.cms_category']) ? $this->services['prestashop.module.link_block.choice_provider.cms_category'] : $this->load('getPrestashop_Module_LinkBlock_ChoiceProvider_CmsCategoryService.php')) && false ?: '_'}->getChoices(), ${($_ = isset($this->services['prestashop.adapter.legacy.context']) ? $this->services['prestashop.adapter.legacy.context'] : $this->getPrestashop_Adapter_Legacy_ContextService()) && false ?: '_'}->getLanguage()->id, ${($_ = isset($this->services['prestashop.adapter.shop.context']) ? $this->services['prestashop.adapter.shop.context'] : ($this->services['prestashop.adapter.shop.context'] = new \PrestaShop\PrestaShop\Adapter\Shop\Context())) && false ?: '_'}->getContextListShopID());
