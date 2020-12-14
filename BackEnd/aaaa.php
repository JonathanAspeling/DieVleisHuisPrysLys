<?php

use Modules\BlockRequestManager\Models\BlockRequest;
use Modules\Constructor\Models\Scope;
use App\User;

$blockRequests = BlockRequest::where('code', 'ilike', 'LA%')->whereNotIn(
    'status',
    [
        'Pending Client Review',
        'Pending Agency Review',
        'Cancelled',
        'Approved'
    ]
)->get();


foreach ($blockRequests as $block) {
    $scope_id = $block['scope_id'];
    $scope = Scope::find($scope_id);
    $drbu = $scope->read()->getMeta()->get('drbu', 'show_ui') . "\n";

    //Detected that Drbu Central was returning 8 Characters when expeting 7. Trim resolves ghost character.

    $route = (trim(strtolower($drbu)) == "central") ? User::getByEmail('juliet.gouldstone@wppteams.com') :
        User::getByEmail('anthony.pounds@wppteams.com');


    $localBlock = \Modules\LocalBlockManager\API\API::newLocalBlock(
        $block->scope->library_id,
        $block->code,
        $route
    );

    $block->local_block_id = $localBlock->id;
    $block->save();
    echo strtolower($drbu) . " completed";
}

